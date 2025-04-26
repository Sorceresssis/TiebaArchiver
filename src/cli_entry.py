def read_tieba_auth() -> None:
    tieba_auth_file_path = os.path.join(os.getcwd(), TIEBA_AUTH_FILENAME)

    try:
        with open(tieba_auth_file_path, "r", encoding="utf-8") as f:
            TiebaAuth.from_dict(orjson.loads(f.read()))
    except Exception:
        BDUSS = questionary.text("未配置BDUSS, 请输入: ").ask()
        TiebaAuth.BDUSS = BDUSS
        with open(tieba_auth_file_path, "w", encoding="utf-8") as f:
            f.write(json_dumps(TiebaAuth.to_dict()))


SCRAPE_CONFIG_FILENAME = "scrape_config.json"
scrape_config_file_path = os.path.join(os.getcwd(), SCRAPE_CONFIG_FILENAME)


def read_scrape_config() -> None:
    try:
        with open(scrape_config_file_path, "r", encoding="utf-8") as f:
            ScrapeConfig.from_dict(orjson.loads(f.read()))
    except FileNotFoundError:
        if questionary.confirm("未找到配置文件, 是否使用默认配置并生成文件?").ask():
            write_scrape_config()
        else:
            sys.exit()
    except orjson.JSONDecodeError:
        if questionary.confirm("配置文件格式错误导致解析失败, 是否使用默认配置并生成文件?").ask():
            write_scrape_config()
        else:
            sys.exit()
    except ValueError as err:
        if questionary.confirm(f"配置变量错误: {str(err)}, 是否使用默认配置并生成文件?").ask():
            write_scrape_config()
        else:
            sys.exit()


def write_scrape_config() -> None:
    with open(scrape_config_file_path, "w", encoding="utf-8") as f:
        f.write(json_dumps(ScrapeConfig.to_dict()))


def set_scrape_config() -> None:
    counter.send((0, 1))
    set_scrape_config_choice = [
        questionary.Choice(
            f"{next(counter)}. 过滤帖子({ScrapeConfigKeys.POST_FILTER_TYPE})",
            ScrapeConfigKeys.POST_FILTER_TYPE,
        ),
        questionary.Choice(
            f"{next(counter)}. 头像保存模式({ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE})",
            ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE,
        ),
        questionary.Choice(
            f"{next(counter)}. 是否爬取转发的原帖({ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN})",
            ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN,
        ),
        questionary.Choice(
            f"{next(counter)}. 是否更新转发的原帖({ScrapeConfigKeys.UPDATE_SHARE_ORIGIN})",
            ScrapeConfigKeys.UPDATE_SHARE_ORIGIN,
        ),
        questionary.Choice(
            f"{next(counter)}. 退出",
            "exit",
        ),
    ]

    while True:
        scrape_config_key = questionary.select("选择配置项", choices=set_scrape_config_choice).ask()
        if ScrapeConfigKeys.POST_FILTER_TYPE == scrape_config_key:
            counter.send((0, 1))
            post_filter_type_choices = [
                questionary.Choice(
                    f"{next(counter)}. '所有的 post' + 'post 下的所有 subpost'({PostFilterType.ALL})",
                    PostFilterType.ALL,
                ),
                questionary.Choice(
                    f"{next(counter)}. 'thread_author 的 post' + 'post 下的所有 subpost'({PostFilterType.AUTHOR_POSTS_WITH_SUBPOSTS})",
                    PostFilterType.AUTHOR_POSTS_WITH_SUBPOSTS,
                ),
                questionary.Choice(
                    f"{next(counter)}. 'thread_author 的 post' + 'post 下 thread_author 的 subpost'({PostFilterType.AUTHOR_POSTS_WITH_AUTHOR_SUBPOSTS})",
                    PostFilterType.AUTHOR_POSTS_WITH_AUTHOR_SUBPOSTS,
                ),
                questionary.Choice(
                    f"{next(counter)}. 'thread_author 的 post 和 thread_author 回复过的 post' + 'post 下所有的 subpost'({PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_SUBPOSTS})",
                    PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_SUBPOSTS,
                ),
                questionary.Choice(
                    f"{next(counter)}. 'thread_author 的 post 和 thread_author 回复过的 post' + 'post 下 thread_author 的 subpost'({PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_AUTHOR_SUBPOSTS})",
                    PostFilterType.AUTHOR_AND_REPLIED_POSTS_WITH_AUTHOR_SUBPOSTS,
                ),
            ]
            post_filter_type = questionary.select("选择帖子过滤模式", choices=post_filter_type_choices).ask()
            ScrapeConfig.POST_FILTER_TYPE = post_filter_type
            write_scrape_config()
        elif ScrapeConfigKeys.DOWNLOAD_USER_AVATAR_MODE == scrape_config_key:
            counter.send((0, 1))
            download_user_avatar_mode_choices = [
                questionary.Choice(
                    f"{next(counter)}. 不保存({DownloadUserAvatarMode.NONE})", DownloadUserAvatarMode.NONE
                ),
                questionary.Choice(
                    f"{next(counter)}. 保存低清({DownloadUserAvatarMode.LOW})", DownloadUserAvatarMode.LOW
                ),
                questionary.Choice(
                    f"{next(counter)}. 保存高清({DownloadUserAvatarMode.HIGH})", DownloadUserAvatarMode.HIGH
                ),
            ]
            download_user_avatar_mode = questionary.select(
                "选择头像保存模式", choices=download_user_avatar_mode_choices
            ).ask()
            ScrapeConfig.DOWNLOAD_USER_AVATAR_MODE = download_user_avatar_mode
            write_scrape_config()
        elif ScrapeConfigKeys.SCRAPE_SHARE_ORIGIN == scrape_config_key:
            scrape_share_origin = questionary.confirm("是否爬取转发的原帖?").ask()
            ScrapeConfig.SCRAPE_SHARE_ORIGIN = scrape_share_origin
            write_scrape_config()
        elif ScrapeConfigKeys.UPDATE_SHARE_ORIGIN == scrape_config_key:
            update_share_origin = questionary.confirm("是否更新转发的原帖?").ask()
            ScrapeConfig.UPDATE_SHARE_ORIGIN = update_share_origin
            write_scrape_config()
        elif "exit" == scrape_config_key:
            break
