import os
import time

from api.aiotieba_api import AioTiebaPosts, get_posts
from config.archive_config import ArchiveConfig
from config.path_config import ThreadDataPathBuilder
from db.content_db import ContentDB
from model.metadata import MetaData
from service.post_service import PostService
from utils.json import json_dumps_to_file


class ArchiveThread:
    def __init__(self, posts: AioTiebaPosts, config: ArchiveConfig):
        self.posts = posts
        self.path_builder = ThreadDataPathBuilder.from_archive(
            posts.forum.fname,
            posts.thread.tid,
            posts.thread.title
        )
        self.config = config

    async def archive(self):
        create_time = int(time.time())

        self._create_metadata(create_time)

        await self._archive_item(self.posts.thread.tid, create_time)
        share_origin = self.posts.thread.share_origin.tid
        if share_origin != 0 and self.config.archive_share_origin:
            print("开始处理 share_origin")
            await self._archive_item(share_origin, create_time, is_share_origin=True)

        duration = int(time.time()) - create_time

        print("任务完成")
        print(f"耗时 {int(duration // 60)} 分 {round(duration % 60, 2)} 秒")
        print(f"帖子数据保存在: {self.path_builder.archive_root}")

    async def _archive_item(self, tid: int, create_time: int, is_share_origin: bool = False):
        if is_share_origin:
            posts = await get_posts(tid)
        else:
            posts = self.posts

        os.makedirs(self.path_builder.get_thread_dir(tid), exist_ok=True)
        db = ContentDB(tid, self.path_builder.get_thread_db(tid))
        logger = self.path_builder.get_thread_log(tid, create_time)
        # thread_service = ThreadService()
        post_service = PostService(self.posts, self.config, db, logger)

        await post_service.archive_posts(self.posts.page.total_page)

        db.close()

    def _create_metadata(self, create_time: int):
        metadata = MetaData(
            create_time=create_time,
            update_time=create_time,
            main_thread=self.posts.thread.tid,
            share_origin=self.posts.thread.share_origin.tid,
            archive_config=self.config,
        )
        json_dumps_to_file(metadata, self.path_builder.get_metadata())
