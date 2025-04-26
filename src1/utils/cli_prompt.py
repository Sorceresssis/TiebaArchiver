from typing import Sequence, Any

import questionary
from prompt_toolkit.styles import Style

prompt_style = Style([
    # 问题标记（?）的样式
    ('qmark', 'fg:cyan bold'),
    # 问题文本的样式
    ('question', 'fg:white bold'),
    # 回答的样式
    ('answer', 'fg:cyan bold'),
    # 选中项的样式
    ('selected', 'fg:cyan bold'),
    # 指示符（>）的样式
    ('pointer', 'fg:cyan bold'),
    # 未选中项的样式
    ('text', ''),
    # 分隔线的样式
    ('separator', 'fg:#ffffff'),
])

SELECT_STYLE = Style([
    ('qmark', 'fg:#3A96DD bold'),
    ('question', 'fg:#3A96DD bold'),
    ('pointer', 'fg:#3A96DD bold'),
    ('answer', 'fg:#3A96DD bold')
])

TEXT_STYLE = Style([
    ('qmark', 'fg:cyan bold'),
    ('question', 'fg:#ffffff bold'),
    ('answer', 'fg:#ffffff bold'),
])

CONFIRM_STYLE = Style([
    # ('qmark', 'fg:#1e90ff bold'),
    # ('question', 'fg:#1e90ff bold'),
    # ('pointer', 'fg:#1e90ff bold'),
    # ('answer', 'fg:#1e90ff bold')
])


class CliPrompt:
    Choice = questionary.Choice

    @staticmethod
    def select(msg: str, choices: Sequence[str | questionary.Choice | dict[str, Any]]):
        return questionary.select(msg, choices=choices, style=SELECT_STYLE)

    @staticmethod
    def text(msg: str):
        return questionary.text(msg, style=TEXT_STYLE)

    @staticmethod
    def confirm(msg: str):
        return questionary.confirm(msg, style=CONFIRM_STYLE)
