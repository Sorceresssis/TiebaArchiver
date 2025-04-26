import functools

import aiotieba as tb
from aiotieba.api.get_comments import UserInfo_c
from aiotieba.api.get_posts import UserInfo_p
from aiotieba.config import ProxyConfig

from config.archive_config import PostFilter
from config.tieba_auth import TiebaAuth
from utils.net import get_system_proxy

AioTiebaPosts = tb.typing.Posts
AioTiebaPostUser = UserInfo_p
AioTiebaSubpostUser = UserInfo_c


def retry(retries: int = 3):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                result = await func(*args, **kwargs)
                if result is None:
                    attempt += 1
                else:
                    return result
            return None

        return wrapper

    return decorator


class AIOTiebaApi:
    def __init__(self, post_filter=PostFilter.ALL):
        proxy = get_system_proxy()
        if proxy is None:
            proxy = False
        else:
            proxy = ProxyConfig(url=f'http://{proxy}')

        self.client = tb.Client(
            TiebaAuth.BDUSS,
            try_ws=True,
            proxy=proxy
        )

        self.only_thread_author = post_filter in [PostFilter.AUTH_W_ALL, PostFilter.AUTH_W_AUTH]

    @retry(3)
    async def get_posts(self, tid: int, pn=1, rn=30):
        async  with self.client as client:
            posts = await client.get_posts(
                tid, pn,
                rn=rn,
                with_comments=True,
                only_thread_author=self.only_thread_author
            )
            if posts.thread.tid:
                return posts
            else:
                return None

    @retry(3)
    async def get_user_threads(self, id_: str | int, pn: int = 1, public_only: bool = False):
        async with self.client as client:
            ts = await client.get_user_threads(id_, pn, public_only=public_only)
            if len(ts.objs) > 0:
                return ts
            else:
                return None


@retry(3)
async def get_posts(tid: int, pn=1, rn=30, post_filter=PostFilter.ALL):
    only_thread_author = False
    if post_filter in [PostFilter.AUTH_W_ALL, PostFilter.AUTH_W_AUTH]:
        only_thread_author = True

    async with tb.Client(TiebaAuth.BDUSS) as client:
        posts = await client.get_posts(tid, pn, rn=rn, with_comments=True, only_thread_author=only_thread_author)
        if posts.thread.tid:
            return posts
        else:
            return None


@retry(3)
async def get_subposts():
    async with tb.Client(TiebaAuth.BDUSS) as client:
        subposts = await client.get_comments()
        if subposts.thread.tid:
            return subposts
        else:
            return None


@retry(3)
async def get_forum(fname_or_fid: str | int):
    async with tb.Client(TiebaAuth.BDUSS) as client:
        forum = await client.get_forum(fname_or_fid)
        if forum.fid:
            return forum
        else:
            return None


@retry(3)
async def get_user_info(id_: str | int):
    async with tb.Client(TiebaAuth.BDUSS) as client:
        user_info = await client.get_user_info(id_)
        # TODO user_id 可能不存在 ,下载测试一下
        if user_info.user_id != 0 or user_info.portrait != "":
            return user_info
        else:
            return None
