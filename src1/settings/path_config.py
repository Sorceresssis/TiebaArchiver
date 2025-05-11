import os
import time
from os import path

from utils.fs import sanitize_filename

# folder_path = dir
# file_path = file

# x_fullname = x_path

# basename = filename | folder_name
# dirname : file, folder 父文件夹的path


a = 'runs/history'
b = 'runs/upgrade'
c = 'runs/readable'
d = 'runs/thread'
e = 'runs/user'


class ThreadDataPathBuilder:
    DATA_FOLDER_NAME = 'archive_data'

    def __init__(self, archive_root):
        self.archive_root = archive_root

    @classmethod
    def from_archive(cls, fname: str, tid: int, title: str, ) -> 'ThreadDataPathBuilder':
        # 不可能超过 255 个字符
        folder_name = cls.get_archive_folder_name(fname, tid, title)
        thread_dir = path.join(
            os.getcwd(),
            cls.DATA_FOLDER_NAME,
            folder_name,
        )
        os.makedirs(thread_dir, exist_ok=True)
        return ThreadDataPathBuilder(thread_dir)

    @classmethod
    def from_update_archive(cls, archive_dir: str) -> 'ThreadDataPathBuilder':
        return ThreadDataPathBuilder(archive_dir)

    @classmethod
    def from_custom_data_dir(cls, data_dir: str, fname: str, tid: int, title: str) -> 'ThreadDataPathBuilder':
        item_dir = path.join(
            data_dir,
            ThreadDataPathBuilder.get_archive_folder_name(fname, tid, title),
        )
        os.makedirs(item_dir, exist_ok=True)
        return ThreadDataPathBuilder(item_dir)

    @staticmethod
    def get_archive_folder_name(fname: str, tid: int, title: str) -> str:
        name = f'[{fname}吧][{tid}]{title}'

        if '\u0590' <= name[-1] <= '\u08FF':  # 如果最后一个字符是从右向左的文字，则添加一个从左向右的标记
            name = name + '\u200E'

        return sanitize_filename(name + f'_{int(time.time())}')

    def get_metadata(self) -> str:
        return path.join(self.archive_root, 'metadata.json')

    def get_content_db(self) -> str:
        return path.join(self.archive_root, 'content.db')

    def get_forum_dir(self, fid: int) -> str:
        return path.join(self.archive_root, 'forums', str(fid))

    def get_users_dir(self):
        return path.join(self.archive_root, 'users')

    def get_logs_dir(self) -> str:
        return path.join(self.archive_root, 'logs')

    def get_log(self) -> str:
        return path.join(self.archive_root, 'logs', f'{int(time.time())}.log')

    def get_thread_images_dir(self, tid: int):
        return path.join(self.archive_root, 'threads', str(tid), 'images')

    def get_thread_videos_dir(self, tid: int):
        return path.join(self.archive_root, 'threads', str(tid), 'videos')

    def get_thread_voices_dir(self, tid: int):
        return path.join(self.archive_root, 'threads', str(tid), 'voices')

    @staticmethod
    def gen_forum_avatar_filename(fid: int):
        return f'f-{fid}_avatar_{int(time.time())}'

    # NOTE 一定要带一个@的前缀，区分其他的数字。
    @staticmethod
    def gen_post_image_filename(pid: int, idx: int):
        return f'p-@{pid}_{idx}'

    @staticmethod
    def gen_post_video_filename(pid: int, idx: int):
        return f'p-@{pid}_{idx}'

    @staticmethod
    def gen_post_voice_filename(pid: int, idx: int, voice_hash: str):
        return f'p-@{pid}_{idx}_{voice_hash}'

    # @staticmethod
    # def get_forum_small_avatar_filename_pattern():
    #     return rf'.*small.*'
    # @staticmethod
    # def get_forum_origin_avatar_filename_pattern():
    #     return rf'.*origin.*'
    # @staticmethod
    # def get_user_avatar_filename(portrait: str):
    #     return f'{portrait}_{get_timestamp()}'
    # @staticmethod
    # def get_user_avatar_filename_pattern(portrait: str):
    #     return rf'.*{portrait}.*'
    # @staticmethod
    # def get_post_assets_filename_pattern(pid: int):
    #     return rf'.*p_{pid}_.*'


class UserDataPathBuilder:

    def __init__(self, item_dir):
        self.item_dir = item_dir

    def get_user_threads_dir(self):
        return path.join(self.item_dir, 'user_threads')

    @staticmethod
    def gen_user_folder_name(nickname: str, user_id: int, ) -> str:
        return f'{nickname}{'' if user_id == 0 else f'[{user_id}]'}_{time.time_ns()}'
