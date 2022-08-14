from src.JsonMap import JsonMap
from src.FileTree import FileTree
import sys
import os


def main():
    if len(sys.argv)>1:
        path = str(sys.argv[1])
        if not os.path.isdir(path):
            raise ValueError("Given Directory does not Exists")
    else:
        path = "."

    path_ob = FileTree(path)
    files_with_status = path_ob.tree_printer(path)
    json_ob = JsonMap(files_with_status)
    print(json_ob.files_json)


if __name__ == "__main__":
    main()
