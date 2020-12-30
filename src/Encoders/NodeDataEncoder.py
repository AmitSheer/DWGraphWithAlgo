import json

from src.NodeData import NodeData


class NodeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NodeData):
            if obj.pos is not None:
                return {
                    'id': obj.key,
                    'pos': obj.pos
                }
            else:
                return {
                    'id': obj.key
                }
        return json.JSONEncoder.default(self, obj)
