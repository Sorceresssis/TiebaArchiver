import os

from config.tieba_auth import TiebaAuth
from utils.cli_prompt import CliPrompt
from utils.json import json_loads_from_file, json_dumps_to_file


class CliTiebaAuthTool:
    FILE_PATH: str = os.path.join(os.getcwd(), "tieba_auth.json")

    loaded: bool = False

    @classmethod
    async def load(cls):
        if cls.loaded:
            return

        try:
            TiebaAuth.from_dict(json_loads_from_file(cls.FILE_PATH))
            cls.loaded = True
        except Exception:
            await cls.modify()

    @classmethod
    async def modify(cls):
        while True:
            bduss = await CliPrompt.text("请输入BDUSS: ").ask_async()
            if not TiebaAuth.verify_bduss(bduss):
                CliPrompt.print("请输入正确的BDUSS")
                continue
            TiebaAuth.BDUSS = bduss
            json_dumps_to_file(TiebaAuth.to_dict(), cls.FILE_PATH)
            break
