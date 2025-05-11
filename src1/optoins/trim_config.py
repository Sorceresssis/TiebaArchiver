from dataclasses import dataclass

from types.archive_config import PostFilter


@dataclass
class TrimConfig:
    post_filter: PostFilter = PostFilter.ALL
    include_user_avatar: bool = True
    include_share_origin: bool = True
