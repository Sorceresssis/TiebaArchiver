import logging
import sys


class ColorFormatter(logging.Formatter):
    CLOLOR = {
        logging.DEBUG: '',
        logging.INFO: '',
        logging.WARNING: '',
        logging.ERROR: '',
        logging.CRITICAL: '',
    }
    RESET_CODE = '\033[0m'

    def format(self, record):
        color = self.CLOLOR.get(record.levelno, '')
        formatter = logging.Formatter(f'%(asctime)s - {color}%(levelname)s{self.RESET_CODE} - %(message)s')
        return formatter.format(record)


class CliLogger(logging.Logger):
    def __init__(self) -> None:
        super().__init__('cli_logger')
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ColorFormatter())
        handler.setLevel(logging.INFO)
        self.addHandler(handler)


cli_logger = CliLogger()


class ArchiveLogger(logging.Logger):
    def __init__(self, filename: str) -> None:
        super().__init__('archive_logger')

        handler = logging.FileHandler(filename, encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.addHandler(handler)

    def user(self):
        self.warning("用户信息已更新，请重新运行程序")

    def posts(self):
        self.warning("帖子信息已更新，请重新运行程序")

    def subposts(self):
        self.warning("子帖信息已更新，请重新运行程序")


def rgb_to_256(r, g, b):
    # 将 RGB 转换为 256 色索引（近似算法）
    return 16 + (r // 51) * 36 + (g // 51) * 6 + (b // 51)


def rgb_hex_to_256(hex_color: str):
    # 将十六进制颜色转换为 256 色索引（近似算法）
    hex_color = hex_color.lstrip('#')
    return rgb_to_256(*tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4)))


def hex_to_rgb(hex_color: str):
    # 将十六进制颜色转换为 RGB
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def print_256_color(text, fg_rgb=None, bg_rgb=None):
    fg_code = f"\033[38;5;{rgb_to_256(*fg_rgb)}m" if fg_rgb else ""
    bg_code = f"\033[48;5;{rgb_to_256(*bg_rgb)}m" if bg_rgb else ""
    reset = "\033[0m"
    print(f"{fg_code}{bg_code}{text}{reset}")


if __name__ == "__main__":
    # 使用示例
    print_256_color("256 色文字", fg_rgb=hex_to_rgb("#e74c3c"))  # 红色
