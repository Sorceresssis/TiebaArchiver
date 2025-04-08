import functools

import aiotieba as tb

from config.archive_config import PostFilter
from tieba_auth import tieba_auth

AioTiebaPosts = tb.typing.Posts


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


@retry(3)
async def get_posts(tid: int, pn=1, rn=30, post_filter=PostFilter.ALL):
    only_thread_author = False
    if post_filter in [PostFilter.AUTH_W_ALL, PostFilter.AUTH_W_AUTH]:
        only_thread_author = True

    async with tb.Client(tieba_auth.BDUSS) as client:
        posts = await client.get_posts(tid, pn, rn=rn, with_comments=True, only_thread_author=only_thread_author)
        if posts.thread.tid:
            return posts
        else:
            return None


@retry(3)
async def get_subposts():
    async with tb.Client(tieba_auth.BDUSS) as client:
        subposts = await client.get_comments()
        if subposts.thread.tid:
            return subposts
        else:
            return None


@retry(3)
async def get_forum(fname_or_fid: str | int):
    async with tb.Client(tieba_auth.BDUSS) as client:
        forum = await client.get_forum(fname_or_fid)
        if forum.fid:
            return forum
        else:
            return None


@retry(3)
async def get_user_info(id_: str | int):
    async with tb.Client(tieba_auth.BDUSS) as client:
        user_info = await client.get_user_info(id_)
        # TODO user_id 可能不存在 ,下载测试一下
        if user_info.user_id != 0 or user_info.portrait != "":
            return user_info
        else:
            return None
