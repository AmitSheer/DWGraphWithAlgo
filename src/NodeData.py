class NodeData:
    def __init__(self, key: int, pos: tuple = None):
        self.key = key
        self.w = 0
        self.parent = None
        self.pos = pos

    def __repr__(self):
        return '{key:' + self.key.__str__() + ', w:' + self.w.__str__() + ', pos:' + self.pos.__str__() + '}'

    def __eq__(self, other):
        return other.key == self.key and \
               self.w == other.w and \
               self.pos == other.pos
