from dataclasses import dataclass, field

from types.archive_config import ArchiveConfig

from __version__ import __version__


@dataclass
class MetaData:
    create_time: int
    update_time: int
    main_thread: int
    share_origin: int
    type: str  # TODO Thread , posts,
    archive_config: ArchiveConfig = field(default_factory=ArchiveConfig)
    platform: str = 'baidu-tieba'
    version: str = __version__
