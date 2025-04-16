from dataclasses import dataclass, field

from config.archive_config import ArchiveConfig
from version import version


@dataclass
class MetaData:
    create_time: int = 0
    update_time: int = 0
    main_thread: int = 0
    share_origin: int = 0
    archive_config: ArchiveConfig = field(default_factory=ArchiveConfig)
    platform: str = 'baidu-tieba'
    version: str = version
