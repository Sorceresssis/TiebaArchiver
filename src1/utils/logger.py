import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logger():
    SUCCESS = 25
    logging.addLevelName(SUCCESS, 'SUCCESS')

    def success(self, message, *args, **kws):
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, message, args, **kws)

    logging.Logger.success = success

    logger = logging.getLogger(__name__)

    # 控制台处理程序
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)  # 记录WARNING和ERROR级别的日志
    console_handler.setFormatter(logging.Formatter(
        f"%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    logger.addHandler(console_handler)

    # 文件处理程序
    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    # file_handler.setLevel(logging.INFO)  #记录所有级别的日志
    file_handler.setFormatter(logging.Formatter(
        f"%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()

logger.debug("Debug 信息（仅文件可见）")
logger.info("Info 信息（文件可见）")
logger.warning("Warning 信息（控制台和文件可见）")
logger.error("Error 信息（控制台和文件可见）")
logger.success("Success 信息（文件可见）")
