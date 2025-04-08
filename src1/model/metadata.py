from dataclasses import dataclass


@dataclass
class MetaData:
    platform: str = 'baidu-tieba'
    platform_name: str = '百度贴吧'
    version: str = ''
    create_time: int = 0
    update_time: int = 0
    main_thread = 0
    share_origin = 0
    archive_config = {}
