import json


class NodeData:
    def __init__(self, key: int, pos: tuple = ()):
        self.key = key
        self.parent = None
        self.pos = pos

    def __repr__(self):
        return '{id:' + self.key.__str__() + ', pos:' + self.pos.__str__() + '}'

    def __eq__(self, other):
        return other.key == self.key and \
               self.pos == other.pos


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeData):
            return {
                'id': obj.key,
                'pos': obj.pos
            }
        return json.JSONEncoder.default(self, obj)
