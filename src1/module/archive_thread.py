import time

from types.archive_config import ArchiveConfig

from api.aiotieba_api import AioTiebaPosts, get_posts
from db.content_db import ContentDB
from model.metadata import MetaData
from settings.path_config import ThreadDataPathBuilder
from utils.json import json_dumps_to_file
from utils.logger import cli_logger, ArchiveLogger


class ArchiveThread:
    def __init__(self, posts: AioTiebaPosts, config: ArchiveConfig):
        self.posts = posts
        self.path_builder = ThreadDataPathBuilder.from_archive(
            posts.forum.fname,
            posts.thread.tid,
            posts.thread.title
        )
        self.config = config
        self.content_db = ContentDB(self.path_builder.get_content_db())
        self.archive_log = ArchiveLogger(self.path_builder.get_log())

    async def archive(self):
        create_time = int(time.time())

        self._create_metadata(create_time)
        await self._archive_item(self.posts.thread.tid, create_time)

        share_origin = self.posts.thread.share_origin.tid
        if share_origin != 0 and self.config.archive_share_origin:
            cli_logger.info("开始处理 share_origin")
            await self._archive_item(share_origin, create_time, is_share_origin=True)

        # user 处理

        duration = int(time.time()) - create_time
        self.content_db.close()

        cli_logger.info("任务完成")
        cli_logger.info(f"耗时 {int(duration // 60)} 分 {round(duration % 60, 2)} 秒")
        cli_logger.info(f"帖子数据保存在: {self.path_builder.archive_root}")
        #

    async def _archive_item(self, tid: int, create_time: int, is_share_origin: bool = False):
        if is_share_origin:
            posts = await get_posts(tid)
            if posts is None:
                # TODO 处理 share_origin 不存在的情况, 处理好这个，有可能只是暂时被删帖，后面可能被恢复，第一次没有找到，第二次ok的情况。
                cli_logger.info(f"share_origin {tid} 不存在")
                return
        else:
            posts = self.posts
        # thread_service = ThreadService()
        # post_service = PostService(self.posts, self.config, db, logger)

        # await post_service.archive_posts(self.posts.page.total_page)

    def _create_metadata(self, create_time: int):
        metadata = MetaData(
            create_time=create_time,
            update_time=create_time,
            main_thread=self.posts.thread.tid,
            share_origin=self.posts.thread.share_origin.tid,
            archive_config=self.config,
        )
        json_dumps_to_file(metadata, self.path_builder.get_metadata())
