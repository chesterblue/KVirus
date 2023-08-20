from engine.listfile import *
from engine.scanfile import *
from engine.filehash import *
from view.console import CLI
import sys
from time import sleep

def gethashes():
    hashes = []
    with open("hash.dat", "r") as fp:
        for hash in fp.readlines():
            hashes.append(hash.strip())
    return hashes

def getfiles(dir):
    GetFiles = ListFile(dir)
    files = GetFiles.get_filenames()
    return files

def scan(dir):
    virusfiles = []
    hashes = gethashes()
    files = getfiles(dir)
    cli = CLI()
    for file in files:
        for virushash in hashes:
            calc = CalcHash(file)
            filehash = calc.calc()
            # cli.in_line("[log] %s hash:%s"%(file,filehash))
            cli.in_line("[log] %s"%(file))
            scan = Scan(filehash, virushash)
            if scan.isVirus():
                cli.new_line("[virus] %s"%file)
                virusfiles.append(file)
    return virusfiles

if __name__ == "__main__":
    try:
        dir = sys.argv[1]
        virusfiles = scan(dir)
    except IndexError:
        print("Please enter path!")