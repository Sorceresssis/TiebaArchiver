import os
import time
from os import path

from utils.fs import sanitize_filename


# folder_path = dir
# file_path = file

# x_fullname = x_path

# basename = filename | folder_name
# dirname : file, folder 父文件夹的path


class ThreadDataPathBuilder:
    DATA_FOLDER_NAME = "archive_data"

    def __init__(self, archive_root):
        self.archive_root = archive_root

    @classmethod
    def from_archive(cls, fname: str, tid: int, title: str) -> "ThreadDataPathBuilder":
        # 不可能超过 255 个字符
        folder_name = sanitize_filename(f"[{fname}吧][{tid}]{title}_{time.time_ns()}")
        thread_dir = path.join(
            os.getcwd(),
            cls.DATA_FOLDER_NAME,
            folder_name,
        )
        os.makedirs(thread_dir, exist_ok=True)
        return ThreadDataPathBuilder(thread_dir)

    @classmethod
    def from_update_archive(cls, archive_dir: str) -> "ThreadDataPathBuilder":
        return ThreadDataPathBuilder(archive_dir)

    @classmethod
    def from_custom_data_dir(cls, data_dir: str, fname: str, tid: int, title: str) -> "ThreadDataPathBuilder":
        item_dir = path.join(
            data_dir,
            ThreadDataPathBuilder.get_archive_folder_name(fname, tid, title),
        )
        os.makedirs(item_dir, exist_ok=True)
        return ThreadDataPathBuilder(item_dir)

    @staticmethod
    def get_archive_folder_name(fname: str, tid: int, title: str) -> str:
        return sanitize_filename(f"[{fname}吧][{tid}]{title}_{time.time_ns()}")

    def get_metadata(self) -> str:
        return path.join(self.archive_root, "metadata.json")

    def get_thread_dir(self, tid: int) -> str:
        return path.join(self.archive_root, "threads", str(tid))

    def get_thread_log(self, tid: int, timestamp: int) -> str:
        return path.join(self.archive_root, "threads", str(tid), "logs", f"{timestamp}.log")

    def get_thread_db(self, tid: int) -> str:
        return path.join(self.archive_root, "threads", str(tid), f"content.db")

    def get_forum_info(self, tid) -> str:
        return path.join(self.archive_root, "threads", str(tid), "forum", "forum.json")

    def get_thread_info(self, tid) -> str:
        return path.join(self.archive_root, "threads", str(tid), "thread.json")

    # ###################################### #

    #
    # def get_forum_avatar_dir(self, tid: int) -> str:
    #     return path.join(self.item_dir, "threads", str(tid), "forum_avatar")
    # def get_user_avatar_dir(self, tid: int):
    #     avatar_dir = path.join(self.item_dir, "threads", str(tid), "user_avatar")
    #     os.makedirs(avatar_dir, exist_ok=True)
    #     return avatar_dir
    #
    # def get_post_assets_dir(self, tid: int) -> str:
    #     return path.join(self.item_dir, "threads", str(tid), "post_assets")
    #
    # def get_post_image_dir(self, tid: int):
    #     image_dir = path.join(self.item_dir, "threads", str(tid), "post_assets", "images")
    #     os.makedirs(image_dir, exist_ok=True)
    #     return image_dir
    #
    # def get_post_video_dir(self, tid: int):
    #     video_dir = path.join(self.item_dir, "threads", str(tid), "post_assets", "videos")
    #     os.makedirs(video_dir, exist_ok=True)
    #     return video_dir
    #
    # def get_post_voice_dir(self, tid: int):
    #     voice_dir = path.join(self.item_dir, "threads", str(tid), "post_assets", "voices")
    #     os.makedirs(voice_dir, exist_ok=True)
    #     return voice_dir
    #
    # @staticmethod
    # def get_forum_small_avatar_filename(forum_name: str):
    #     return f"f_{forum_name}_small-avatar_{get_timestamp()}"
    #
    # @staticmethod
    # def get_forum_small_avatar_filename_pattern():
    #     return rf".*small.*"
    #
    # @staticmethod
    # def get_forum_origin_avatar_filename(forum_name: str):
    #     return f"f_{forum_name}_origin-avatar_{get_timestamp()}"
    #
    # @staticmethod
    # def get_forum_origin_avatar_filename_pattern():
    #     return rf".*origin.*"
    #
    # @staticmethod
    # def get_user_avatar_filename(portrait: str):
    #     return f"{portrait}_{get_timestamp()}"
    #
    # @staticmethod
    # def get_user_avatar_filename_pattern(portrait: str):
    #     return rf".*{portrait}.*"
    #
    # @staticmethod
    # def get_post_image_filename(pid: int, idx: int):
    #     return f"p_{pid}_{idx}_{get_timestamp()}"
    #
    # @staticmethod
    # def get_post_video_filename(pid: int, idx: int):
    #     return f"p_{pid}_{idx}_{get_timestamp()}"
    #
    # @staticmethod
    # def get_post_voice_filename(pid: int, idx: int, voice_hash: str):
    #     return f"p_{pid}_{idx}_{voice_hash}"
    #
    # @staticmethod
    # def get_post_assets_filename_pattern(pid: int):
    #     return rf".*p_{pid}_.*"


class UserDataPathBuilder:

    def __init__(self, item_dir):
        self.item_dir = item_dir

    def get_user_threads_dir(self):
        return path.join(self.item_dir, "user_threads")

    @staticmethod
    def gen_user_folder_name(nickname: str, user_id: int, ) -> str:
        return f"{nickname}{"" if user_id == 0 else f"[{user_id}]"}_{time.time_ns()}"
