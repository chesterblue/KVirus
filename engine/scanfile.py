

class Scan():
    def __init__(self, filehash, virushash: str) -> None:
        self.filehash = filehash
        self.virus = virushash

    def isVirus(self):
        if self.filehash == self.virus:
            return True
        else:
            return False
        
class MutltiThreadScan():
    def __init__(self, virushashs: list) -> None:
        self.virus = virushashs

    