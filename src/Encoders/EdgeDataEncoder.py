import json

from src.EdgeData import EdgeData


class EdgeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EdgeData):
            return {
                'src': obj.src,
                'dest': obj.dest,
                'w': obj.w
            }
        return json.JSONEncoder.default(self, obj)