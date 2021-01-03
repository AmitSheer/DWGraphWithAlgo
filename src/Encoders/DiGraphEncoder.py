import json
from src.DiGraph import DiGraph
from src.Encoders.EdgeDataEncoder import EdgeDataEncoder
from src.Encoders.NodeDataEncoder import NodeDataEncoder


class DiGraphEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DiGraph):
            node_data = NodeDataEncoder()
            edge_data = EdgeDataEncoder()
            return {
                'Nodes': [node_data.default(x) for x in list(obj.get_all_v().values())],
                'Edges': [edge_data.default(x) for x in obj.get_edges()]
            }
        return json.JSONEncoder.default(self, obj)
