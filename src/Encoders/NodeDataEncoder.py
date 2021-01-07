import itertools
import json
from src.NodeData import NodeData


class Data(list):
    def __init__(self, iterable):
        super().__init__()
        self.iterable = iter(iterable)
        try:
            self.firstitem = next(self.iterable)
            self.truthy = True
        except StopIteration:
            self.truthy = False

    def __iter__(self):
        if not self.truthy:
            return iter([])
        return itertools.chain([self.firstitem], self.iterable)

    def __len__(self):
        raise NotImplementedError("Fakelist has no length")

    def __getitem__(self, i):
        raise NotImplementedError("Fakelist has no getitem")

    def __setitem__(self, i, **kwargs):
        raise NotImplementedError("Fakelist has no setitem")

    def __bool__(self):
        return self.truthy


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeData):
            if obj.get_pos() is not None:
                return {
                    'id': obj.get_key(),
                    'pos': obj.get_location().__str__()
                }
            else:
                return {
                    'id': obj.get_key()
                }
        return json.JSONEncoder.default(self, obj)
