import asyncio

from api.aiotieba_api import get_posts
from module.archive_thread import ArchiveThread


async def archive_thread(tid: int):
    # verification_posts
    v_posts = await get_posts(tid, 1)
    if v_posts is None:
        "\n".join(
            [
                "预加载错误，可能是以下原因:",
                "1. 连接错误，请多尝试几次。",
                "2. 网络故障，请检查网络。",
                "3. tid 错误, 请检查是否输入正确",
                "4. 帖子可能已被屏蔽或删除",
                "5. BDUSS 失效，请重新配置",
            ]
        ),
        return

    archiver = ArchiveThread(v_posts, {})
    await archiver.archive()


if __name__ == '__main__':
    asyncio.run(archive_thread(tid=9628951031))
