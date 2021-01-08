from random import random
from typing import IO

from src import layout
from src.DiGraph import DiGraph
from src.Encoders.NodeDataEncoder import *
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphPloter import *
from src.algorithms.Dijkstra import dijkstra
from src.algorithms.Trajan import *
from src.fruchterman_reingold import fruchterman_reingold


# from main import shit


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = None):
        super()
        self.sccList: List[list] = []
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def copy_graph(self) -> DiGraph:
        g = DiGraph()
        for node in self.graph.get_all_v().values():
            g.add_node(node.get_key(), node.get_pos())
        for node in self.graph.get_all_v():
            for key, w in self.graph.all_out_edges_of_node(node).items():
                g.add_edge(node, key, w)
        return g

    def load_from_json(self, file_name: str) -> bool:
        fs: IO
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
                        pos_tuple = (float(pos.split(',')[0]), float(pos.split(',')[1]), float(pos.split(',')[2]))
                        graph.add_node(id, pos_tuple)
                    except:
                        graph.add_node(id, None)
                except:
                    return False
            for edge in j['Edges']:
                graph.add_edge(edge['src'], edge['dest'], edge['w'])
            self.graph = graph
            fs.close()
            return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as json_file:
                json_file.write('{"Nodes": ')
                json.dump(Data(self.graph.get_all_v().values()), json_file, cls=NodeDataEncoder)
                json_file.write(', "Edges": ')
                edges = [{'src': node_id, 'dest': int(dest), 'w': w} for node_id in self.graph.get_all_v() for dest, w
                         in self.graph.all_out_edges_of_node(node_id).items()]
                json.dump(edges, json_file)
                # for node_id in self.graph.get_all_v():
                #     for dest, w in self.graph.all_out_edges_of_node(node_id).items():
                #         json.dump({'src': node_id, 'dest': int(dest), 'w': float(w)}, json_file)
                json_file.write('}')
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
        node: NodeData = self.graph.get_all_v().get(id2)
        nodes_path.append(node.get_key())
        while node.get_parent() is not None:
            nodes_path.append(node.get_parent().get_key())
            node = node.get_parent()
        node = self.graph.get_all_v().get(id2)
        nodes_path.reverse()
        if len(nodes_path) == 1:
            return node.get_dist(), []
        return node.get_dist(), nodes_path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        self.reset()
        scc = trajan(self.graph, id1)
        for c in scc:
            if id1 in [a.get_key() for a in c]:
                return c

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
        g: DiGraph = self.copy_graph()
        # vortex_with_no_point = [node for node in g.get_all_v().values()]
        vortex_with_no_point = [node for node in g.get_all_v().values() if
                                node.get_pos() is None or node.get_pos() == (None, None, None)]
        if len(vortex_with_no_point) == self.graph.v_size() and g.v_size() > 0:
            layout.circle(g)
            for i in range(50):
                for v in g.get_all_v().values():
                    v.dx = 0
                    v.dy = 0
                fruchterman_reingold(g)
            # layout.center_and_scale(g, 10, 10)
        elif len(vortex_with_no_point) > 0:
            frame = get_frame(self.graph)
            W = abs(frame[1] - frame[0])
            L = abs(frame[3] - frame[2])
            for node in vortex_with_no_point:
                n = g.get_all_v().get(node.get_key())
                n.set_pos((frame[0] + W * random(), frame[2] + L * random(), 0))
        plotter(g)

    def reset(self):
        for node in list(self.graph.get_all_v().values()):
            node.set_dist(float('inf'))
            node.set_parent(None)
