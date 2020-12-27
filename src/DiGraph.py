from GraphInterface import GraphInteface
from src.EdgeData import EdgeData
from src.NodeData import NodeData


class DiGraph(GraphInteface):
    def __init__(self):
        super()
        self.nodes = dict()
        self.edges = dict()
        self.edges_into = dict()
        self.edges_size = 0
        self.mc = 0

    def v_size(self) -> int:
        return self.nodes.__len__()

    def e_size(self) -> int:
        return self.edges_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edges_into.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)

    def get_mc(self) -> int:
        return self.mc

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
                self.nodes.get(id1) is not None and \
                self.nodes.get(id2) is not None and \
                id1 != id2:
            e = EdgeData(id1, id2, weight)
            if self.edges_into.get(id2).get(id1) is None:
                self.edges_size += 1
            else:
                if self.edges.get(id1).get(id2).get_w() == weight:
                    return True
            self.mc += 1
            self.edges.get(id1).__setitem__(id2, e)
            self.edges_into.get(id2).__setitem__(id1, e)
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id) is None:
            self.nodes.__setitem__(node_id, NodeData(node_id, pos))
            self.edges.__setitem__(node_id, dict())
            self.edges_into.__setitem__(node_id, dict())
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if self.nodes.get(node_id) is not None:
            edges = self.all_in_edges_of_node(node_id).copy()
            for edge in edges:
                self.remove_edge(edge, node_id)
            self.edges_into.pop(node_id)
            edges = self.all_out_edges_of_node(node_id).copy()
            for edge in edges:
                self.remove_edge(node_id, edge)
            self.edges.pop(node_id)
            self.nodes.pop(node_id)
            self.mc -= 1
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
        if self.edges.get(node_id1) is not None:
            node: dict = self.edges.get(node_id1)
            if node.get(node_id2) is not None:
                self.edges.get(node_id1).pop(node_id2)
                self.edges_into.get(node_id2).pop(node_id1)
                self.mc += 1
                self.edges_size -= 1
                return True
        return False
