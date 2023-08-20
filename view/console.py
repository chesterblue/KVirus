import sys
from colorama.win32 import (
        FillConsoleOutputCharacter,
        GetConsoleScreenBufferInfo,
        STDOUT,
)
class CLI():
    def __init__(self) -> None:
        self.last_in_line = False

    def clearLine(self):
        """
        备注：文件名太长导致高度问题等待解决
        """
        csbi = GetConsoleScreenBufferInfo()
        line = "\b" * int(csbi.dwCursorPosition.X)
        sys.stdout.write(line)
        width = csbi.dwCursorPosition.X
        csbi.dwCursorPosition.X = 0
        FillConsoleOutputCharacter(STDOUT, " ", width, csbi.dwCursorPosition)
        sys.stdout.write(line)
        sys.stdout.flush()

    def in_line(self, string):
        self.clearLine()
        sys.stdout.write(string)
        sys.stdout.flush()
        self.last_in_line = True

    def new_line(self, string=""):
        if self.last_in_line:
            self.clearLine()
        
        sys.stdout.write(string)
        sys.stdout.flush()
        sys.stdout.write("\r\n")
        sys.stdout.flush()

        sys.stdout.flush()
        self.last_in_line = False
        sys.stdout.flush()
        