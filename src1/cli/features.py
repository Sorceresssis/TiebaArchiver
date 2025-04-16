from enum import IntEnum, auto
from typing import List, Dict, Any


class ProgramFeatures(IntEnum):
    ARCHIVE_THREAD = auto()
    UPDATE_ARCHIVED_THREAD = auto()
    EXPORT_TO_READABLE = auto()
    MODIFY_CONFIG = auto()
    MODIFY_TIEBA_AUTH = auto()
    EXIT = auto()
    ARCHIVE_USER_THREADS = auto()
    UPDATE_ARCHIVED_USER_THREADS = auto()

    # 绕过用户隐藏，不一定能成功，力迫耗时。
    ARCHIVE_USER_THREADS_BYPASS = auto()
    UPDATE_ARCHIVED_USER_THREADS_BYPASS = auto()

    # TODO POST_THREADS 如果保存？
    #  将用户的回复过的 THREADS 完完整整的保存还是，只保存大致 thread 信息和用户的回复内容。
    ARCHIVED_USER_THREADS_AND_POST_THREADS = auto()
    UPDATE_ARCHIVED_USER_THREADS_AND_POST_THREADS = auto()


program_features: List[Dict[str, Any]] = [
    {
        "value": ProgramFeatures.ARCHIVE_THREAD,
        "title": "💾 归档帖子",
    },
    {
        "value": ProgramFeatures.UPDATE_ARCHIVED_THREAD,
        "title": "🔄 更新已归档帖子",
    },
    {
        "value": ProgramFeatures.EXPORT_TO_READABLE,
        "title": "📄 导出归档数据为可读文件",
    },
    {
        "value": ProgramFeatures.MODIFY_CONFIG,
        "title": "⚙️ 修改归档配置",
    },
    {
        "value": ProgramFeatures.MODIFY_TIEBA_AUTH,
        "title": "🔑 更新贴吧登录信息(BDUSS)",
    },
    {
        "value": ProgramFeatures.EXIT,
        "title": "🚪 退出程序",
    },
    {
        "value": ProgramFeatures.ARCHIVE_USER_THREADS,
        "title": "👤 归档用户的主题帖",
        "disabled": "未实现"
    },
]
