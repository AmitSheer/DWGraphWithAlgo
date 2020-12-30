import json


class EdgeData:
    def __init__(self, src: int, dest: int, w: float):
        self.src = src
        self.dest = dest
        self.w = w
        self.type = -1

    def __repr__(self):
        return "{src:" + self.src.__str__() + ", dest:" + self.dest.__str__() + ", w:" + self.w.__str__() + "}"

    def __eq__(self, other):
        return other.dest == self.dest and \
               other.src == self.src and \
               other.w == self.w



