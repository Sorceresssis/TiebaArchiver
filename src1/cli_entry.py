import asyncio
import logging

import colorama

from __version__ import __version__
from cli.archive_thread import archive_thread
from cli.features import ProgramFeatures, program_features
from cli.tieba_auth_tool import CliTiebaAuthTool
from utils.cli_prompt import CliPrompt

colorama.init(autoreset=True)
colorama.just_fix_windows_console()

loggers = logging.Logger.manager.loggerDict
for logger_name in loggers:
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.handlers = []


def main():
    print(f'TiebaArchive v{__version__}')

    features_select = CliPrompt.select(
        '※ 选择功能',
        choices=list(map(lambda x: CliPrompt.Choice(
            f'{x['value']}. {x['title']}', x['value'], x['disabled'] if 'disabled' in x else None
        ), program_features)),
    )

    while True:
        print('\n')
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


if __name__ == '__main__':
    main()
