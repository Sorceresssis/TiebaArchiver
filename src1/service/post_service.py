import asyncio
from logging import Logger

from types.archive_config import ArchiveConfig, PostFilter

from api.aiotieba_api import AioTiebaPosts, get_posts, get_subposts
from db.content_db import ContentDB
from db.post_dao import PostDao
from service.user_service import UserService
from utils.pcp import PCP

# 多余
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

    def test_update_post(self, posts: AioTiebaPosts):

        for post in posts.objs:
            if not post.is_thread_author and self.config.post_filter in [
                PostFilter.AUTH_W_ALL,
                PostFilter.AUTH_W_AUTH,
                PostFilter.AUTH_RPL_W_ALL,
                PostFilter.AUTH_RPL_W_AUTH,
            ]:
                continue

            is_new_post = True  # 查询

            if len(post.comments) > 0:
                self.test_update_subpost(post.pid, is_new_post)

            if is_new_post:
                # add
                pass
            else:
                # update
                pass

    async def test_update_subpost(self, pid: int, is_new_post: bool = False):
        subposts = await get_subposts()
        for subpost in subposts.objs:
            if not subpost.is_thread_author and self.config.post_filter in [
                PostFilter.AUTH_RPL_W_ALL,
                PostFilter.AUTH_RPL_W_AUTH
            ]:
                continue

            if is_new_post:
                # add
                pass
            else:
                # update

                pass
