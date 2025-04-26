from dataclasses import dataclass, field

from __version__ import VERSION
from config.archive_config import ArchiveConfig


@dataclass
class MetaData:
    create_time: int
    update_time: int
    main_thread: int
    share_origin: int
    archive_config: ArchiveConfig = field(default_factory=ArchiveConfig)
    platform: str = 'baidu-tieba'
    version: str = VERSION
