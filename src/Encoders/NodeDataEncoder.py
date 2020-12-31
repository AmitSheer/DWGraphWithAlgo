import json

from src.NodeData import NodeData


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeData):
            if obj.get_pos() is not None:
                return {
                    'id': obj.get_key(),
                    'pos': obj.get_pos().__str__()
                }
            else:
                return {
                    'id': obj.get_key()
                }
        return json.JSONEncoder.default(self, obj)
