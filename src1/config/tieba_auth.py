from typing import Dict


class TiebaAuth:
    BDUSS: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> None:
        bduss = data.get("BDUSS")
        if not cls.verify_bduss(bduss):
            raise ValueError("BDUSS 错误")
        cls.BDUSS = bduss

    @classmethod
    def to_dict(cls) -> Dict[str, str]:
        return {"BDUSS": cls.BDUSS}

    @staticmethod
    def verify_bduss(bduss: str) -> bool:
        # BDUSS 192 个字符
        # STOKEN 64 个字符
        return len(bduss) == 192
