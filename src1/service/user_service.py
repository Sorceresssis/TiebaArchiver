from logging import Logger

from config.archive_config import ArchiveConfig
from db.content_db import ContentDB


class UserService:
    def __init__(self, tid: int, config: ArchiveConfig, db: ContentDB, logger: Logger):
        self.tid = tid
        self.config = config
        self.db = db
        self.logger = logger
