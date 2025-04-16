from dataclasses import dataclass
from enum import IntEnum, auto


class ContentFragType(IntEnum):
    """
    text
    emojis
    imgs
    ats
    links
    tiebapluses
    video	视频碎片
    voice
    """

    TEXT = auto()
    EMOJI = auto()
    IMAGE = auto()
    AT = auto()
    LINK = auto()
    TIEBAPLUS = auto()
    VIDEO = auto()
    VOICE = auto()

    SCRAPE_ERROR = -1


@dataclass
class ContentFrag:
    type: int


# NOTE 这是一个非常特殊的frag, 它不是贴吧原有的内容, 而是用于标记爬取过程中出现错误的分块
@dataclass
class FragScrapeError(ContentFrag):
    error_frag_type: int
    error_frag_name: str


@dataclass
class FragText(ContentFrag):
    text: str


@dataclass
class FragEmoji(ContentFrag):
    id: str
    desc: str


@dataclass
class FragImage(ContentFrag):
    filename: str
    tb_origin_src: str  # tieba 的原图链接
    origin_size: int  # 通常是0
    show_width: int
    show_height: int
    hash: str


@dataclass
class FragAt(ContentFrag):
    text: str
    user_id: int


@dataclass
class FragLink(ContentFrag):
    text: str
    title: str
    raw_url: str


@dataclass
class FragTiebaPlus(ContentFrag):
    """
    贴吧plus广告碎片

    Attributes:
        text (str): 贴吧plus广告描述
        url (yarl.URL): 解析后的贴吧plus广告跳转链接
    """

    text: str = ""
    url: str = ""


@dataclass
class FragVideo(ContentFrag):
    filename: str
    cover_filename: str
    duration: int
    width: int
    height: int
    view_num: int

    tb_origin_src: str
    tb_origin_cover_src: str


@dataclass
class FragVoice(ContentFrag):
    filename: str
    md5: str
    duration: int
    tb_origin_src: str


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


@dataclass
class UserEntity:
    id: int
    portrait: str | None = None
    username: str | None = None
    nickname: str = ""
    tieba_uid: int | None = None

    avatar: str | None = None
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
    status: int = UserStatus.ACTIVE

    completed: int = 0  # (v1.3.0) 新增: 0 | 1
    scrape_time: int = 0  # (v1.3.0) 新增


@dataclass
class TiebaOriginSrcEntity:
    filename: str
    content_frag_type: int
    origin_src: str
