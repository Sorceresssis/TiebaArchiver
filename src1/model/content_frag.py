from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Dict


class ContentFragType(IntEnum):
    ERROR = -1

    TEXT = 1
    EMOJI = auto()
    IMAGE = auto()
    AT = auto()
    LINK = auto()
    TIEBA_PLUS = auto()
    VIDEO = auto()
    VOICE = auto()

    @classmethod
    def labels(cls) -> Dict['ContentFragmentType', str]:
        if not hasattr(cls, '_label_map'):
            cls._label_map = {
                cls.ERROR: "error",
                cls.TEXT: "text",
                cls.EMOJI: "emoji",
                cls.IMAGE: "image",
                cls.AT: "at",
                cls.LINK: "link",
                cls.TIEBA_PLUS: "tieba_plus",
                cls.VIDEO: "video",
                cls.VOICE: "voice",
            }
        return cls._label_map

    @property
    def label(self) -> str:
        """获取标准化类型标签（兼容旧版数据）"""
        return self.labels().get(self)


@dataclass
class ContentFrag:
    type: int


# NOTE 这是一个非常特殊的frag, 它不是贴吧原有的内容, 而是用于标记爬取过程中出现错误的分块
@dataclass
class FragError(ContentFrag):
    error_frag_type: int
    error_frag_label: str


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
