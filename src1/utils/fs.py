import os
import re


def sanitize_filename(filename: str, replacement: str = '', windows_reserved_suffix='_') -> str:
    """
    去除文件名中的非法字符，并返回新的文件名.
    """
    # \x00-\x1F     控制字符
    # \x7F          DEL 删除控制符
    # \\/:*?"<>|    不能作为文件名的字符
    sanitized_filename = re.sub(r'[\x00-\x1F\x7F\\/:*?"<>|]', replacement, filename)

    sanitized_filename = sanitized_filename.strip()

    # 处理 Windows 保留文件名
    # https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    if os.name == 'nt':
        reserved_names = ['CON', 'PRN', 'AUX', 'NUL', 'CONIN$', 'CONOUT$']
        reserved_names.extend([f'COM{i}' for i in range(1, 10)])
        reserved_names.extend([f'LPT{i}' for i in range(1, 10)])

        if sanitized_filename.upper() in reserved_names:
            sanitized_filename = sanitized_filename + windows_reserved_suffix

    return sanitized_filename
