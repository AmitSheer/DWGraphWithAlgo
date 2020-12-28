class NodeData:
    def __init__(self, key: int, pos: tuple = None):
        self.key = key
        self.w = 0
        self.parent = None
        self.pos = pos

    def get_key(self) -> int:
        return self.key

    def get_w(self) -> float:
        return self.w

    def get_pos(self) -> tuple:
        return self.pos

    def get_parent(self):
        return self.parent

    def __eq__(self, other):
        return other.get_key() == self.get_key() and \
               self.get_w() == other.get_w() and\
               self.get_pos() == other.get_pos()
