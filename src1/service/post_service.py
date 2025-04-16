import asyncio
from logging import Logger

from api.aiotieba_api import AioTiebaPosts, get_posts
from config.archive_config import ArchiveConfig
from db.content_db import ContentDB
from db.post_dao import PostDao
from service.user_service import UserService
from utils.pcp import PCP

lock = asyncio.Lock()


class PostService:
    def __init__(self, tid: int, config: ArchiveConfig, db: ContentDB, logger: Logger):
        self.tid = tid
        self.config = config
        self.db = db
        self.logger = logger

        self.dao = PostDao(db)
        self.user_service = UserService(tid, config, db, logger)

        self.total_page = 0

        self.pn = 0

    async def p(self):
        async with lock:
            self.pn += 1
            if self.pn > self.total_page:
                self.pn = 0
            return self.pn

    async def archive_posts(self, total_page: int, *, is_update: bool = False):
        self.total_page = total_page

        await PCP(
            min(10, total_page),
            min(3, total_page),
            8,
            8,
            self.fetch_posts,
            self.save_posts,
        ).run()

    async def save_posts(self, posts: AioTiebaPosts):
        print(posts)

    async def fetch_posts(self):
        pn = await self.p()

        if pn != 0:
            return await get_posts(self.posts.thread.tid, pn)
        else:
            return None

    def save_subpost(self):
        pass

    def fetch_subpost(self):
        pass
