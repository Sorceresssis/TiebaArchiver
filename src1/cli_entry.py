import asyncio

import colorama as clr

from cli.archive_thread import archive_thread
from cli.features import ProgramFeatures, program_features
from cli.tieba_auth_tool import CliTiebaAuthTool
from utils.cli_prompt import CliPrompt
from version import version

clr.init(autoreset=True)
clr.just_fix_windows_console()


def print_tips():
    print(clr.Style.BRIGHT + clr.Fore.CYAN + f"TiebaArchive {version}")
    print("\n")


def main():
    print_tips()

    features_select = CliPrompt.select(
        "※ 选择功能",
        choices=list(map(lambda x: CliPrompt.Choice(
            f"{x['value']}. {x['title']}", x['value'], x['disabled'] if 'disabled' in x else None
        ), program_features)),
    )

    while True:
        selected_features = features_select.ask()

        if ProgramFeatures.ARCHIVE_THREAD == selected_features:
            asyncio.run(archive_thread())
        elif ProgramFeatures.UPDATE_ARCHIVED_THREAD == selected_features:
            pass
        elif ProgramFeatures.EXPORT_TO_READABLE == selected_features:
            pass
        elif ProgramFeatures.MODIFY_CONFIG == selected_features:
            pass
        elif ProgramFeatures.MODIFY_TIEBA_AUTH == selected_features:
            asyncio.run(CliTiebaAuthTool.modify())
        elif ProgramFeatures.EXIT == selected_features:
            break

        print("\n")


if __name__ == "__main__":
    main()
