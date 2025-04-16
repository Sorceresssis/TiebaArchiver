from dataclasses import dataclass
from enum import StrEnum
from typing import Dict, Any


class UserAvatarSave(StrEnum):
    NO = "no"
    LOW = "low"
    HIGH = "high"

    @property
    def label(self) -> str:
        return {
            UserAvatarSave.NO: "不下载",
            UserAvatarSave.LOW: "低清",
            UserAvatarSave.HIGH: "高清",
        }[self]


class PostFilter(StrEnum):
    # all_posts + all_subposts
    ALL = "all"
    # author_posts + all_subposts
    AUTH_W_ALL = "auth_w_all"
    # author_posts + author_subposts
    AUTH_W_AUTH = "auth_w_auth"
    # author_and_replied_posts + all_subposts
    AUTH_RPL_W_ALL = "auth_rpl_w_all"
    # author_and_replied_posts + author_subposts
    AUTH_RPL_W_AUTH = "auth_rpl_w_auth"

    @property
    def label(self) -> str:
        return {
            PostFilter.ALL: "全部",
            PostFilter.AUTH_W_ALL: "作者 + 全部子串",
            PostFilter.AUTH_W_AUTH: "作者 + 作者子串",
            PostFilter.AUTH_RPL_W_ALL: "作者 + 全部子串 + 全部回复",
            PostFilter.AUTH_RPL_W_AUTH: "作者 + 作者子串 + 作者回复",
        }[self]


@dataclass
class ArchiveConfig:
    # All
    post_filter: PostFilter = PostFilter.ALL
    user_avatar_save: UserAvatarSave = UserAvatarSave.HIGH
    archive_share_origin: bool = True

    # First Archive

    # Update Archive
    update_share_origin: bool = True  # 仅当 archive_share_origin 为 True 时，此配置项才生效

    def insight(self) -> str:
        # TODO 展示
        return "\n".join([
            f"回复帖筛选方式(post_filter): {self.post_filter.label}",
            f"头像保存设置(user_avatar_save): {self.user_avatar_save.label}",
            f"是否保留帖子来源信息(archive_share_origin): {self.archive_share_origin}",
            f"更新转发原主题帖(update_share_origin): {self.update_share_origin}",
        ])

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        # TODO 验证
        try:
            return ArchiveConfig(
                post_filter=PostFilter(data.get("post_filter", PostFilter.ALL)),
                user_avatar_quality=UserAvatarQuality(data.get("download_user_avatar", UserAvatarQuality.HIGH)),
                archive_share_origin=data.get("archive_share_origin", True),
                update_share_origin=data.get("update_share_origin", True),
            )
        except Exception as e:
            print(e)
            raise ValueError("Invalid archive config")
