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
                'Nodes': [node_data.default(x) for x in list(obj.nodes.values())],
                'Edges': [edge_data.default(y) for x in obj.edges.values() for y in x.values()]
            }
        return json.JSONEncoder.default(self, obj)
