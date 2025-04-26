from dataclasses import dataclass
from enum import StrEnum
from typing import Dict, Any


class UserAvatarSave(StrEnum):
    NO = "no"
    LOW = "low"
    HIGH = "high"

    @classmethod
    def labels_cn(cls) -> Dict['UserAvatarSave', str]:
        if not hasattr(cls, '_label_map_cn'):
            cls._label_map_cn = {
                UserAvatarSave.NO: "不下载",
                UserAvatarSave.LOW: "低清",
                UserAvatarSave.HIGH: "高清",
            }
        return cls._label_map_cn

    @property
    def label_cn(self) -> str:
        return self.labels_cn().get(self)


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

    @classmethod
    def labels_cn(cls) -> Dict['PostFilter', str]:
        if not hasattr(cls, '_label_map_cn'):
            cls._label_map_cn = {
                PostFilter.ALL: "全部",
                PostFilter.AUTH_W_ALL: "作者回复帖 + 全部子贴",
                PostFilter.AUTH_W_AUTH: "作者 + 作者子串",
                PostFilter.AUTH_RPL_W_ALL: "作者 + 全部子串 + 全部回复",
                PostFilter.AUTH_RPL_W_AUTH: "作者 + 作者子串 + 作者回复",
            }
        return cls._label_map_cn

    @property
    def label_cn(self) -> str:
        return self.labels_cn().get(self)


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
            f"回复帖筛选方式(post_filter): {self.post_filter.label_cn}",
            f"头像保存设置(user_avatar_save): {self.user_avatar_save.label}",
            f"是否保留帖子来源信息(archive_share_origin): {self.archive_share_origin}",
            f"更新转发原主题帖(update_share_origin): {self.update_share_origin}",
        ])

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        #
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

# from typing import List, Tuple, get_type_hints
#
# class DBInfo:
#     version: str
#
#     @classmethod
#     def from_tuples(cls, tuples: List[Tuple[str, str]]):
#         # 获取类定义的类型注解
#         type_hints = get_type_hints(cls)
#
#         # 校验数据结构有效性
#         cls._validate_tuples(tuples, type_hints)
#
#         # 设置属性值
#         processed_keys = set()
#         for k, v in tuples:
#             # 类型转换校验
#             v = cls._cast_value_type(k, v, type_hints)
#
#             setattr(cls, k, v)
#             processed_keys.add(k)
#
#         # 检查必填字段
#         cls._check_required_fields(type_hints, processed_keys)
#
#     @classmethod
#     def _validate_tuples(cls, tuples: List[Tuple[str, str]], type_hints: dict):
#         """执行多级数据校验"""
#         allowed_keys = type_hints.keys()
#         seen_keys = set()
#
#         for idx, (k, v) in enumerate(tuples):
#             # 校验键名格式
#             if not k.isidentifier():
#                 raise ValueError(f"Invalid key format at position {idx}: '{k}'")
#
#             # 校验键名合法性
#             if k not in allowed_keys:
#                 raise KeyError(f"Unexpected key '{k}' at position {idx}. "
#                                f"Allowed keys: {list(allowed_keys)}")
#
#             # 检测重复键
#             if k in seen_keys:
#                 raise ValueError(f"Duplicate key '{k}' at position {idx}")
#             seen_keys.add(k)
#
#     @classmethod
#     def _cast_value_type(cls, key: str, value: str, type_hints: dict):
#         """执行类型转换与校验"""
#         target_type = type_hints.get(key)
#         if not target_type:
#             return value
#
#         try:
#             # 处理基础类型转换
#             if target_type is str:
#                 return str(value)
#             elif target_type is int:
#                 return int(value)
#             elif target_type is float:
#                 return float(value)
#             elif target_type is bool:
#                 return value.lower() in ('true', '1', 'yes')
#             # 添加更多类型处理逻辑...
#         except ValueError as e:
#             raise TypeError(
#                 f"Type conversion failed for key '{key}'. "
#                 f"Expected {target_type.__name__}, got {value!r}"
#             ) from e
#
#     @classmethod
#     def _check_required_fields(cls, type_hints: dict, processed_keys: set):
#         """检查必填字段"""
#         required_fields = {k for k, t in type_hints.items()
#                            if not isinstance(t, type(None))}
#         missing = required_fields - processed_keys
#         if missing:
#             raise ValueError(f"Missing required fields: {missing}")
