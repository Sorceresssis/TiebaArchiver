import os
import time

from api.aiotieba_api import AioTiebaPosts
from config.path_config import ThreadDataPathBuilder
from model.metadata import MetaData


class ArchiveThread:
    def __init__(self, posts: AioTiebaPosts, config: dict):
        self.posts = posts
        self.path_builder = ThreadDataPathBuilder.from_archive_thread(
            posts.forum.fname,
            posts.thread.tid,
            posts.thread.title
        )
        self.config = config

        timestamp: int
        batch: int

    async def archive(self):
        start_time = time.time()

        self._create_metadata()

        await self._archive_item(self.posts.thread.tid)

        if self.posts.thread.share_origin.tid != 0:
            await self._archive_item(self.posts.thread.share_origin.tid)

        int(start_time)

        end_time = time.time()

        duration = end_time - start_time

    async def _archive_item(self, tid: int, timestamp: int):
        os.makedirs(self.path_builder.get_thread_dir(tid), exist_ok=True)

        db = self.path_builder.get_content_db_path(tid)
        logger = self.path_builder.get_scrape_log_path(tid, int(time.time()))

        db.close()

    def _create_metadata(self):
        self.path_builder.get_metadata_path()
        MetaData()
