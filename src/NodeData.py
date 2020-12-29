import json
import sys


class NodeData:
    key: int
    pos: tuple

    def __init__(self, key: int, pos: tuple = ()):
        self.key = key
        if pos is not None:
            self.pos = pos
        else:
            self.pos = ()
        # params for algorithms
        self.parent = None
        self.type = -1
        self.dist = sys.maxsize
        self.visited = False
        self.index = None
        self.low_link = None

    def __repr__(self):
        return '{id:' + self.key.__str__() + ', pos:' + self.pos.__str__() + '}'

    def __eq__(self, other):
        return other.dist == self.dist


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeData):
            return {
                'id': obj.key,
                'pos': obj.pos
            }
        return json.JSONEncoder.default(self, obj)
