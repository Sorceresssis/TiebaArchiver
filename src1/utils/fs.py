import re

extname_map = {
    '.mp3': ['MP3', 'MPEG-1 Audio Layer 3'],
    '.wav': ['WAVE'],
    '.ogg': ['Ogg'],
    '.flac': ['FLAC'],
    '.aac': ['AAC'],
    '.m4a': ['MPEG-4 Audio'],
    '.wma': ['Windows Media Audio'],
    '.amr': ['Adaptive Multi-Rate'],
    '.mp4': ['MP4'],
    '.jpg': ['JPEG'],
    '.jpeg': ['JPEG'],
}


def file_type_to_extname(file_type: str) -> str:
    for extname, file_types in extname_map.items():
        if file_type in file_types:
            return extname


def sanitize_filename(filename: str, replacement: str = '', windows_reserved_suffix='_') -> str:
    """
    去除文件名中的非法字符，并返回新的文件名.
    """
    # \x00-\x1F     控制字符
    # \x7F          DEL 删除控制符
    # \\/:*?"<>|    不能作为文件名的字符
    sanitized_filename = re.sub(r'[\x00-\x1F\x7F\\/:*?"<>|]', replacement, filename)

    sanitized_filename = sanitized_filename.strip()

    # 处理 Windows 保留文件名 https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    reserved_names = ['CON', 'PRN', 'AUX', 'NUL', 'CONIN$', 'CONOUT$']
    reserved_names.extend([f'COM{i}' for i in range(1, 10)])
    reserved_names.extend([f'LPT{i}' for i in range(1, 10)])
    if sanitized_filename.upper() in reserved_names:
        sanitized_filename = sanitized_filename + windows_reserved_suffix

    return sanitized_filename
