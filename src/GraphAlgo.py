import json
import sys

from typing import List
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Encoders.DiGraphEncoder import DiGraphEncoder
from src.algorithms.Dijkstra import dijkstra
from src.algorithms.Trajan import trajan


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = None):
        super()
        self.sccList: List[list] = []
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            fs = open(file_name, 'r')
            j = json.load(fs)
            for node in j['Nodes']:
                id: int
                try:
                    id = node['id']
                    try:
                        pos = node['pos']
                        graph.add_node(id, pos)
                    except:
                        graph.add_node(id, None)
                except:
                    return False
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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        self.reset()
        dijkstra(self.graph.get_all_v().get(id1), id2, self.graph)
        nodes_path = []
        node = self.graph.get_all_v().get(id2)
        nodes_path.append(node.key)
        while node.parent is not None:
            nodes_path.append(node.parent.key)
            node = node.parent
        node = self.graph.get_all_v().get(id2)
        nodes_path.reverse()
        return node.dist, nodes_path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        self.reset()
        return trajan(self.graph, id1).pop()

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        self.reset()
        return trajan(self.graph)


    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError

    def reset(self):
        for node in list(self.graph.get_all_v().values()):
            node.dist = sys.maxsize
            node.visited = False
            node.parent = None
            node.type = -1
            node.index = None
            node.low_link = None
            for edge in list(self.graph.all_out_edges_of_node(node.key).values()):
                edge.type = -1




