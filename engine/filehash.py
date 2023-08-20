import hashlib

class CalcHash():
    """
    calculate hash of file
    """
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.hash = ""

    def calc(self):
        m = hashlib.md5()
        with open(self.filepath, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                m.update(data)
        self.hash =  m.hexdigest()
        return self.hash

class MultiThreadCalcHash():
    def __init__(self) -> None:
        pass