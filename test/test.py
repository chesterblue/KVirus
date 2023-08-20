from time import sleep
from console import CLI
test = []
cli = CLI()
for i in test:
    sleep(0.3)
    cli.in_line("[log] %s "%(i))


# import os
# files = []

# def list_files(path) -> None:
#         for entry in os.scandir(path):
#             if entry.is_file():
#                 files.append(entry.path)
#             elif entry.is_dir():
#                 list_files(entry.path)

# list_files("D:\\testpython")
# # print(files)
# for i in files:
#     sleep(0.3)
#     cli.in_line("[log] %s "%(i))
# import hashlib
# def calc():
#     m = hashlib.md5()
#     with open(r"", 'rb') as f:
#         while True:
#             data = f.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     hash =  m.hexdigest()
#     return hash

# print(calc())