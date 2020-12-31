import json

from src.EdgeData import EdgeData


class EdgeDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EdgeData):
            return {
                'src': obj.get_src(),
                'dest': obj.get_dest(),
                'w': obj.get_w()
            }
        return json.JSONEncoder.default(self, obj)