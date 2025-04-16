import os

from orjson import orjson

from config.archive_config import ArchiveConfig
from utils.cli_prompt import CliPrompt
from utils.json import json_loads_from_file, json_dumps_to_file


class CliArchiveConfigTool:
    FILE_PATH: str = os.path.join(os.getcwd(), "archive_config.json")

    loaded: bool = False
    user_archive_config: ArchiveConfig = ArchiveConfig()

    @classmethod
    async def load(cls) -> ArchiveConfig:
        if not cls.loaded:
            try:
                cls.user_archive_config = ArchiveConfig.from_dict(json_loads_from_file(cls.FILE_PATH))
            except FileNotFoundError:
                cls.save()
            except orjson.JSONDecodeError:
                if await CliPrompt.confirm('配置文件格式错误导致解析失败, 使用默认配置?').ask_async():
                    cls.save()
            except ValueError:
                if await CliPrompt.confirm('配置变量错误，使用默认配置?').ask_async():
                    cls.save()

        cls.loaded = True
        return cls.user_archive_config

    @classmethod
    async def edit_user_archive_config(cls) -> None:
        new_config = await cls.editor(cls.user_archive_config)
        cls.user_archive_config = new_config
        cls.save()

    @classmethod
    def save(cls) -> None:
        json_dumps_to_file(cls.user_archive_config, cls.FILE_PATH)

    @staticmethod
    async def editor(config: ArchiveConfig) -> ArchiveConfig:
        pass

# def set_scrape_config() -> None:
#     counter.send((0, 1))
#     set_scrape_config_choice = [
#         questionary.Choice(
#             f"{next(counter)}. 过滤帖子({ScrapeConfigKeys.POST_FILTER_TYPE})",
#             ScrapeConfigKeys.POST_FILTER_TYPE,
#         ),
#         questionary.Choice(
#             f"{next(counter)}. 头像保存模式({ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE})",
#             ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE,
#         ),
#         questionary.Choice(
#             f"{next(counter)}. 是否爬取转发的原帖({ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN})",
#             ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN,
#         ),
#         questionary.Choice(
#             f"{next(counter)}. 是否更新转发的原帖({ScrapeConfigKeys.UPDATE_SHARE_ORIGIN})",
#             ScrapeConfigKeys.UPDATE_SHARE_ORIGIN,
#         ),
#         questionary.Choice(
#             f"{next(counter)}. 退出",
#             "exit",
#         ),
#     ]

#     while True:
#         scrape_config_key = questionary.select("选择配置项", choices=set_scrape_config_choice).ask()
#         if ScrapeConfigKeys.POST_FILTER_TYPE == scrape_config_key:
#             counter.send((0, 1))
#             post_filter_type_choices = [
#                 questionary.Choice(
#                     f"{next(counter)}. '所有的 post' + 'post 下的所有 subpost'({PostFilterType.ALL})",
#                     PostFilterType.ALL,
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 'thread_author 的 post' + 'post 下的所有 subpost'({PostFilterType.AUTHOR_POSTS_WITH_SUBPOSTS})",
#                     PostFilterType.AUTHOR_POSTS_WITH_SUBPOSTS,
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 'thread_author 的 post' + 'post 下 thread_author 的 subpost'({PostFilterType.AUTHOR_POSTS_WITH_AUTHOR_SUBPOSTS})",
#                     PostFilterType.AUTHOR_POSTS_WITH_AUTHOR_SUBPOSTS,
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 'thread_author 的 post 和 thread_author 回复过的 post' + 'post 下所有的 subpost'({PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_SUBPOSTS})",
#                     PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_SUBPOSTS,
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 'thread_author 的 post 和 thread_author 回复过的 post' + 'post 下 thread_author 的 subpost'({PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_AUTHOR_SUBPOSTS})",
#                     PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_AUTHOR_SUBPOSTS,
#                 ),
#             ]
#             post_filter_type = questionary.select("选择帖子过滤模式", choices=post_filter_type_choices).ask()
#             ScrapeConfig.POST_FILTER_TYPE = post_filter_type
#             write_scrape_config()
#         elif ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE == scrape_config_key:
#             counter.send((0, 1))
#             download_user_avatar_mode_choices = [
#                 questionary.Choice(
#                     f"{next(counter)}. 不保存({DownloadUserAvatarMode.NONE})", DownloadUserAvatarMode.NONE
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 保存低清({DownloadUserAvatarMode.LOW})", DownloadUserAvatarMode.LOW
#                 ),
#                 questionary.Choice(
#                     f"{next(counter)}. 保存高清({DownloadUserAvatarMode.HIGH})", DownloadUserAvatarMode.HIGH
#                 ),
#             ]
#             download_user_avatar_mode = questionary.select(
#                 "选择头像保存模式", choices=download_user_avatar_mode_choices
#             ).ask()
#             ScrapeConfig.DOWNLOAD_USER_AVATAR_MODE = download_user_avatar_mode
#             write_scrape_config()
#         elif ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN == scrape_config_key:
#             scrape_share_origin = questionary.confirm("是否爬取转发的原帖?").ask()
#             ScrapeConfig.SCRAPE_SHARE_ORIGIN = scrape_share_origin
#             write_scrape_config()
#         elif ScrapeConfigKeys.UPDATE_SHARE_ORIGIN == scrape_config_key:
#             update_share_origin = questionary.confirm("是否更新转发的原帖?").ask()
#             ScrapeConfig.UPDATE_SHARE_ORIGIN = update_share_origin
#             write_scrape_config()
#         elif "exit" == scrape_config_key:
#             break
