from dataclasses import dataclass
from enum import StrEnum
from typing import Dict, Any


class DownloadUserAvatar(StrEnum):
    NO = "no"
    LOW = "low"
    HIGH = "high"

    @property
    def label(self) -> str:
        return {
            DownloadUserAvatar.NO: "不下载",
            DownloadUserAvatar.LOW: "低清",
            DownloadUserAvatar.HIGH: "高清",
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
    # 全适用
    save_user_extra_info: bool = True
    post_filter: PostFilter = PostFilter.ALL
    download_user_avatar: DownloadUserAvatar = DownloadUserAvatar.HIGH

    # fist
    archive_share_origin: bool = True

    # update
    update_share_origin: bool = True  # 如果 archive_share_origin为 False, 则不更新 share_origin
    fill_missing_share_origin: bool = False  # 是否追加 share_origin, 如果初次archive 时没有 archive_share_origin
    update_user_info: bool = False  # 更新用户的 nickname, sign, traffic 信息.不包含avatar

    def insight(self) -> str:
        return "\n".join([
            f"保存用户额外信息(save_user_extra_info): {self.save_user_extra_info}({self.save_user_extra_info})",
            f"post_filter: {self.post_filter.label}",
            f"download_user_avatar: {self.download_user_avatar.label}",
            f"archive_share_origin: {self.archive_share_origin}",
            f"update_share_origin: {self.update_share_origin}",
            f"fill_missing_share_origin: {self.fill_missing_share_origin}",
        ])

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return ArchiveConfig(
            save_user_extra_info=data.get("save_user_extra_info", True),
            post_filter=PostFilter(data.get("post_filter", PostFilter.ALL)),
            download_user_avatar=DownloadUserAvatar(data.get("download_user_avatar", DownloadUserAvatar.HIGH)),
            archive_share_origin=data.get("archive_share_origin", True),
            update_share_origin=data.get("update_share_origin", True),
        )


if __name__ == "__main__":
    print(ArchiveConfig().insight())
