import sys
from colorama.win32 import (
        FillConsoleOutputCharacter,
        GetConsoleScreenBufferInfo,
        STDOUT,
)

def clearLine():
    csbi = GetConsoleScreenBufferInfo()
    line = "\b" * int(csbi.dwCursorPosition.X)
    sys.stdout.write(line)
    width = csbi.dwCursorPosition.X
    csbi.dwCursorPosition.X = 0
    FillConsoleOutputCharacter(STDOUT, " ", width, csbi.dwCursorPosition)
    sys.stdout.write(line)
    sys.stdout.flush()

def newLine(string ="", add = True):
    clearLine()
    if add:
        sys.stdout.write(string)
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
    else:
        sys.stdout.write(string)
        sys.stdout.flush()

for i in range(1000):
    if i in [5,30,45,85]:
         newLine(str(i))
    else:
        newLine(str(i),add=False)