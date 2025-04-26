from logging import Logger

from api.aiotieba_api import AioTiebaPostUser, AioTiebaSubpostUser
from config.archive_config import ArchiveConfig
from db.content_db import ContentDB


class UserService:
    def __init__(self, tid: int, config: ArchiveConfig, db: ContentDB, logger: Logger):
        self.tid = tid
        self.config = config
        self.db = db
        self.logger = logger

    def reg_from_post_user(self, user: AioTiebaPostUser):
        if user.user_id == 0:
            return

    def reg_from_subpost_user(self, user: AioTiebaSubpostUser):
        if user.user_id == 0:
            return

    def reg_from_at(self, user_id: int, nickname: str):
        if user_id == 0:
            return

    def reg_from_id(self, user_id: int):
        if user_id == 0:
            return

    def complete(self):
        # 查询当前批次的用户
        # TODO 删除没有关联的user
        pass
