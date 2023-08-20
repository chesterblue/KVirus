import os


class ListFile():
    def __init__(self, rootpath) -> None:
        self.rootpath = rootpath
        self.files = []
    
    def get_filenames(self) -> list:
        self.list_files(self.rootpath)
        return self.files

    def list_files(self, path) -> None:
        for entry in os.scandir(path):
            if entry.is_file():
                self.files.append(entry.path)
            elif entry.is_dir():
                self.list_files(entry.path)