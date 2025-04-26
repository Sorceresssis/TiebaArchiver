from dataclasses import dataclass


@dataclass
class PostEntity:
    id: int
    contents: str
    floor: int  # 楼和楼中楼一样
    user_id: int
    agree: int
    disagree: int
    create_time: int
    is_thread_author: bool
    sign: str = ""  # 楼独有, 小尾巴
    reply_num: int = 0  # 楼独有, 回复数
    # 楼中楼独有, 区分楼和楼中楼的唯一标识 where parent_id = 0
    parent_id: int = 0
    # 楼中楼独有, 也不是所有的楼中楼都有这个字段, 对应的是楼中楼的作者user_id, 不是post_id
    reply_to_id: int = 0

    scrape_batch_id: int = 0  # (v1.3.1) 新增


from dataclasses import dataclass
from enum import IntEnum, auto


class UserStatus(IntEnum):
    ACTIVE = 0  # 正常
    DEACTIVATED = auto()  # 注销


class UserInfoCompleteness(IntEnum):
    ID = 10
    AT = 20
    POST_CARRY = 30
    USER_INFO = 40


@dataclass
class UserEntity:
    id: int
    portrait: str | None = None
    tieba_uid: int | None = None
    username: str | None = None
    nickname: str = ""

    glevel: int = 0
    gender: int = 0
    ip: str = ""
    is_vip: bool = False
    is_god: bool = False
    age: float = 0
    sign: str = ""
    post_num: int = 0
    agree_num: int = 0
    fan_num: int = 0
    follow_num: int = 0
    forum_num: int = 0

    level: int = 0
    is_bawu: bool = False

    avatar: str = ''
    batch: int = 0
    completeness: UserInfoCompleteness = UserInfoCompleteness.ID
    done: bool = False


@dataclass
class TiebaOriginSrcEntity:
    filename: str
    content_frag_type: int
    origin_src: str
