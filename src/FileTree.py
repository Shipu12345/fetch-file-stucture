import os
from src.FileStatus import FileStatus

class FileTree:
    def __init__(self, root) -> None:
        self.root = root

    def tree_printer(self, root):
        files_dict = {}
        for every in os.scandir(root):
            if os.path.isdir(every):
                files_dict[every.name]=self.tree_printer(every)
            else:
                files_dict[every.name]=FileStatus.Untouched
        return files_dict
