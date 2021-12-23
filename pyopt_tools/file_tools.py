# file_tools.py has useful functions for working with files
import os


def get_size(file_path: str, size_in="") -> str:
    """
    Returns file size in gb/mb/kb/bytes
    :param  file_path: path to the file
    :param  size_in: gb/mb/kb/bytes (if not set default would be its original size)
    :return: file size in gb/mb/kb/bytes

        Example:
            >>> get_size("test.txt")
            >>> "8.98 KB"
            >>> get_size("test.txt", size_in="bytes")
            >>> "9200 bytes"
    """
    if size_in == "":
        size = os.path.getsize(file_path)
        if size > 1024 ** 3:
            size = size / 1024 ** 3
            return f"{size:.2f} GB"
        elif size > 1024 ** 2:
            size = size / 1024 ** 2
            return f"{size:.2f} MB"
        elif size > 1024:
            size = size / 1024
            return f"{size:.2f} KB"
        else:
            return f"{size} bytes"
    else:
        size = os.path.getsize(file_path)
        if size_in == "gb":
            size = size / 1024 ** 3
            return f"{size:.2f} GB"
        elif size_in == "mb":
            size = size / 1024 ** 2
            return f"{size:.2f} MB"
        elif size_in == "kb":
            size = size / 1024
            return f"{size:.2f} KB"
        elif size_in == "bytes":
            return f"{size} bytes"
        else:
            raise ValueError(f"{size_in} is not a valid size type")


def find_in_files(folder_path: str, search_string: str, file_types: list = None, case_sensitive: bool = False) -> list:
    """
    Returns a list of files that contains the given string and the line number and also the entire line that contains.
    :param folder_path: path to the folder
    :param search_string: string to search for
    :param file_types file_types to target (optional)
    :param case_sensitive: if True will search case-sensitive
    :return: list of files that contains the given string and the line number and also the entire line that contains

        Example:
            >>> find_in_files("/home/user/Desktop", "test")
            >>> [["test.txt", 1, "test"], ["test2.txt", 2, "test"]]

    """
    if file_types is None:
        file_types = []
    files = []
    if not file_types:
        for file in os.listdir(folder_path):
            with open(os.path.join(folder_path, file), "r") as f:
                for i, line in enumerate(f):
                    if case_sensitive:
                        if search_string in line:
                            files.append([file, i + 1, line])
                    else:
                        if search_string.lower() in line.lower():
                            files.append([file, i + 1, line])
    else:
        for file_type in file_types:
            for file in os.listdir(folder_path):
                if file.endswith(file_type):
                    with open(os.path.join(folder_path, file), "r") as f:
                        for i, line in enumerate(f):
                            if case_sensitive:
                                if search_string in line:
                                    files.append([file, i + 1, line])
                            else:
                                if search_string.lower() in line.lower():
                                    files.append([file, i + 1, line])
    return files



