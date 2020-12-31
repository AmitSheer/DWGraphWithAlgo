import json

from src.GraphInterface import GraphInterface
from src.EdgeData import EdgeData
from src.NodeData import NodeData
from src.Encoders import EdgeDataEncoder, NodeDataEncoder
from typing import Dict, List


class DiGraph(GraphInterface):
    def __init__(self):
        super()
        self.__nodes: Dict[int, NodeData] = dict()
        self.__edges: Dict[int, Dict[int, EdgeData]] = dict()
        self.__edges_into: Dict[int, Dict[int, EdgeData]] = dict()
        self.__edges_size = 0
        self.__mc = 0

    def get_node(self, key: int) -> NodeData:
        return self.__nodes.get(key)

    def get_edges(self) -> List[EdgeData]:
        return [edge for node_edges in self.__edges.values() for edge in node_edges.values()]

    def v_size(self) -> int:
        return len(self.__nodes)

    def e_size(self) -> int:
        return self.__edges_size

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        edges: Dict[int, float] = {}
        for edge in self.__edges_into.get(id1).values():
            edges.__setitem__(edge.get_src(), edge.get_w())
        return edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        edges: Dict[int, float] = {}
        for edge in self.__edges.get(id1).values():
            edges.__setitem__(edge.get_dest(), edge.get_w())
        return edges

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
                Adds an edge to the graph.
                @param id1: The start node of the edge
                @param id2: The end node of the edge
                @param weight: The weight of the edge
                @return: True if the edge was added successfully, False o.w.
                Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
                """
        if weight >= 0 and \
                self.__nodes.get(id1) is not None and \
                self.__nodes.get(id2) is not None and \
                id1 != id2:
            e = EdgeData(id1, id2, weight)
            if self.__edges_into.get(id2).get(id1) is None:
                self.__edges_size += 1
            else:
                if self.__edges.get(id1).get(id2).get_w() == weight:
                    return True
            self.__mc += 1
            self.__edges.get(id1).__setitem__(id2, e)
            self.__edges_into.get(id2).__setitem__(id1, e)
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.__nodes.get(node_id) is None:
            self.__nodes.__setitem__(node_id, NodeData(node_id, pos))
            self.__edges.__setitem__(node_id, dict())
            self.__edges_into.__setitem__(node_id, dict())
            self.__mc += 1
            return True
        return False

    def add_node_as_nodedata(self, node: NodeData) -> bool:
        if self.__nodes.get(node.key) is None:
            self.__nodes.__setitem__(node.key, node)
            self.__edges.__setitem__(node.key, dict())
            self.__edges_into.__setitem__(node.key, dict())
            self.__mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if self.__nodes.get(node_id) is not None:
            edges = self.all_in_edges_of_node(node_id).copy()
            for edge in edges:
                self.remove_edge(edge, node_id)
            self.__edges_into.pop(node_id)
            edges = self.all_out_edges_of_node(node_id).copy()
            for edge in edges:
                self.remove_edge(node_id, edge)
            self.__edges.pop(node_id)
            self.__nodes.pop(node_id)
            self.__mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if self.__edges.get(node_id1) is not None:
            node: dict = self.__edges.get(node_id1)
            if node.get(node_id2) is not None:
                self.__edges.get(node_id1).pop(node_id2)
                self.__edges_into.get(node_id2).pop(node_id1)
                self.__mc += 1
                self.__edges_size -= 1
                return True
        return False

    def __repr__(self):
        edges = []
        for edge in self.__edges.values():
            for e in edge.values():
                edges.append(e)
        return '{ Nodes: ' + str(list(self.__nodes.values())) + ', Edges:' + str(edges) + '}'

    def __eq__(self, other):
        return self.__nodes == other.__nodes and self.__edges == other.__edges
