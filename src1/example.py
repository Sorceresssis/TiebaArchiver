import asyncio

from api.aiotieba_api import get_posts
from config.archive_config import ArchiveConfig, UserAvatarSave, PostFilter
from config.tieba_auth import TiebaAuth
from module.archive_thread import ArchiveThread


async def archive_thread(tid: int):
    # ANCHOR 1. 设置 BDUSS
    TiebaAuth.BDUSS = ""

    # ANCHOR 2. 预加载，判断帖子是否存在，
    v_posts = await get_posts(tid, 1)
    if v_posts is None:
        # 错误原因
        # "1. 连接错误，请多尝试几次。",
        # "2. 网络故障，请检查网络。",
        # "3. tid 错误, 请检查是否输入正确",
        # "4. 帖子可能已被屏蔽或删除",
        # "5. BDUSS 失效，请重新配置",
        return

    # ANCHOR 3. 创建 ArchiveConfig 对象，并设置相关配置
    # 默认配置
    # config = ArchiveConfig()

    # 自定义配置
    config = ArchiveConfig(
        post_filter=PostFilter.AUTH_W_ALL,  # only_thread_author
        user_avatar_save=UserAvatarSave.NO,  # 不下载用户头像
    )

    # ANCHOR 4. 创建 ArchiveThread 任务对象，并调用 archive 方法进行归档
    archiver = ArchiveThread(v_posts, config)
    await archiver.archive()


if __name__ == '__main__':
    asyncio.run(archive_thread(9633288686))
