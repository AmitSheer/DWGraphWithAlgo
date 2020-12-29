import json
import heapq
import sys

from typing import List
from src.DiGraph import DiGraph, DiGraphEncoder
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


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
        self.dijkstra(self.graph.get_all_v().get(id1), id2)
        nodes_path = []
        node = self.graph.get_all_v().get(id2)
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
        self.trajan(id1)
        return self.sccList.pop()

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        self.trajan()
        return self.sccList

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

    def dijkstra(self, start: NodeData, key_to_find: int):
        self.reset()
        start.dist = 0
        # counter for how many visited
        visited = 0

        # using tuple here so the values won change
        unvisited_queue = [(start.dist, start)]
        heapq.heapify(unvisited_queue)

        while len(unvisited_queue) and visited != self.graph.v_size():
            current_node = heapq.heappop(unvisited_queue)[1]
            if current_node.visited is False:
                current_node.visited = True
                if key_to_find == current_node.key:
                    return
                for edge in self.graph.all_out_edges_of_node(current_node.key).values():
                    if (edge.w + current_node.dist) < self.graph.get_all_v().get(edge.dest).dist:
                        self.graph.get_all_v().get(edge.dest).dist = edge.w + current_node.dist
                        self.graph.get_all_v().get(edge.dest).parent = current_node
                        unvisited_queue.append(
                            (self.graph.get_all_v().get(edge.dest).dist, self.graph.get_all_v().get(edge.dest)))
                heapq.heapify(unvisited_queue)

    def trajan(self, node_id: int = None):
        self.reset()
        stack = []
        self.index = 0
        if node_id is None:
            for node in list(self.graph.get_all_v().values()):
                if node.index is None:
                    self.dfs(node, stack)
        else:
            self.dfs(self.graph.get_all_v().get(node_id), stack)

    # def tarjan_for_single_node(self, node_id):

    def dfs(self, curr: NodeData, stack):
        curr.low_link = self.index
        curr.index = self.index
        curr.visited = True
        stack.append(curr)
        curr.index = self.index
        self.index += 1
        for n in list([self.graph.get_all_v().get(edge.dest)] for edge in
                      self.graph.all_out_edges_of_node(curr.key).values()):
            node = n.pop()
            if node.index is None:
                self.dfs(node, stack)
                curr.low_link = min(curr.low_link, node.low_link)
            elif node.visited:
                curr.low_link = min(curr.low_link, node.index)
        if curr.low_link == curr.index:
            scc = []
            while len(stack):
                popped_node = stack.pop()
                popped_node.visited = False
                scc.append(popped_node)
                if popped_node == curr:
                    break
            self.sccList.append(scc)
