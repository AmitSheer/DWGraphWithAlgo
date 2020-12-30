import sys


class NodeData:
    key: int
    pos: tuple

    def __init__(self, key: int, pos: tuple = None):
        self.key = key
        self.pos = pos
        # params for algorithms
        self.parent = None
        self.type = -1
        self.dist = sys.maxsize
        self.visited = False
        self.index = None
        self.low_link = None

    def __repr__(self):
        if self.pos is not None:
            return '{id:' + self.key.__str__() + ', pos:' + self.pos.__str__() + '}'
        else:
            return '{id:' + self.key.__str__() + '}'

    def __eq__(self, other):
        return other.dist == self.dist and other.pos == self.pos and other.key == self.key
