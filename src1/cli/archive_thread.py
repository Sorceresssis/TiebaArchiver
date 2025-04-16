import re

from api.aiotieba_api import get_posts
from cli.archive_config_tool import CliArchiveConfigTool
from cli.tieba_auth_tool import CliTiebaAuthTool
from module.archive_thread import ArchiveThread
from utils.cli_prompt import CliPrompt


async def archive_thread():
    # TODO log archive

    await CliTiebaAuthTool.load()
    config = await CliArchiveConfigTool.load()

    ids_str = input("请输入帖子ID (多个请用空格/换行分隔)：")
    if not re.match(r'^[\d\s\n]+$', ids_str):
        print("请输入正确的tid")
        return

    print(config.insight())
    if not await CliPrompt.confirm("使用该配置还是修改").ask_async():
        config = await CliArchiveConfigTool.editor(config)

    failures = []
    for id_str in ids_str.split():
        tid = int(id_str)

        v_posts = await get_posts(tid, 1)
        if v_posts is None:
            print("预加载错误")
            failures.append(tid)
            continue

        archiver = ArchiveThread(v_posts, config)
        await archiver.archive()

    if len(failures) > 0:
        print("以下帖子加载失败，请检查tid是否正确")
        print(failures)
        print("Tips: 加载错误，可能是以下原因")
        print("\n".join([
            "   1. 连接错误，可多尝试几次。",
            "   2. 网络故障，请检查网络通畅。",
            "   3. tid 错误, 请检查是否输入正确",
            "   4. 帖子可能已被屏蔽或删除",
            "   5. BDUSS 已失效，请重新配置",
        ]))
