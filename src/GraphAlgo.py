import json
from src.DiGraph import DiGraph, DiGraphEncoder
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        super()
        self.graph = GraphInterface()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            fs = open(file_name, 'r')
            j = json.load(fs)
            for node in j['Nodes']:
                graph.add_node(node['id'], node['pos'])
            for edge in j['Edges']:
                graph.add_edge(edge['src'], edge['dest'], edge['w'])
            self.graph = graph
            return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as json_file:
                json.dump(self.graph, json_file, cls=DiGraphEncoder)
                return True
        except:
            return False