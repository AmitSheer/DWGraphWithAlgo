import os
import sys
import unittest
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData


class TestGraphAlgo(unittest.TestCase):
    def setUp(self):
        self.graph = DiGraph()

    def test_get_graph(self):
        self.graph = DiGraph()
        for i in range(10):
            self.graph.add_node(i)
        graph_algo = GraphAlgo(self.graph)
        self.assertEqual(self.graph.__str__(), graph_algo.get_graph().__str__())

    def test_load_from_json(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(1, 3, 1.8)
        self.graph.add_edge(2, 3, 1.1)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json('../data/T0.json')
        self.assertEqual(self.graph, graph_algo.get_graph())

    def test_save_to_json(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(1, 3, 1.8)
        self.graph.add_edge(2, 3, 1.1)
        graph_algo = GraphAlgo(self.graph)
        graph_algo.save_to_json('test.json')
        try:
            with open('test.json') as fp:
                saved_file = fp.read()
                fp.close()
            with open('../data/T0.json') as fp:
                T0 = fp.read()
                fp.close()
            self.assertEqual(saved_file, T0)
        finally:
            os.remove('test.json')

    def test_shortest_path(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(2, 3, 1.1)
        graph_algo = GraphAlgo(self.graph)
        shortest_path: List[list] = graph_algo.shortest_path(1, 3)
        self.assertEqual((2.4000000000000004, [1, 2]), shortest_path)
        self.graph.add_edge(1, 3, 1.8)
        shortest_path: List[list] = graph_algo.shortest_path(1, 3)
        self.assertEqual((1.8, [1]), shortest_path)

    def test_shortest_path_not_connected_nodes(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(1, 3, 1.8)
        self.graph.add_edge(2, 3, 1.1)
        self.graph.add_node(4)
        graph_algo = GraphAlgo(self.graph)
        shortest_path: List[list] = graph_algo.shortest_path(1, 4)
        self.assertEqual((float('inf'), []), shortest_path)

    def test_connected_component(self):
        self.graph = DiGraph()
        for i in range(5):
            self.graph.add_node(i)
        # 0 <-> 1
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        #  2
        self.graph.add_edge(1, 2, 1.3)
        # 3 <-> 4
        self.graph.add_edge(4, 3, 1.1)
        self.graph.add_edge(3, 4, 1.1)
        algo = GraphAlgo(self.graph)
        scc: list = algo.connected_component(0)
        self.assertEqual([NodeData(1), NodeData(0)], scc)
        scc: list = algo.connected_component(1)
        self.assertEqual([NodeData(0),NodeData(1)], scc)
        scc: list = algo.connected_component(2)
        self.assertEqual([NodeData(2)], scc)
        scc: list = algo.connected_component(4)
        self.assertEqual([NodeData(3),NodeData(4)], scc)

    def test_connected_components(self):
        self.graph = DiGraph()
        for i in range(5):
            self.graph.add_node(i)
        # 0 <-> 1
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        #  2
        self.graph.add_edge(1, 2, 1.3)
        # 3 <-> 4
        self.graph.add_edge(4, 3, 1.1)
        self.graph.add_edge(3, 4, 1.1)
        algo = GraphAlgo(self.graph)
        scc: list = algo.connected_components()
        self.assertTrue(scc.__contains__([NodeData(2)]))
        self.assertTrue(scc.__contains__([NodeData(1), NodeData(0)]))
        self.assertTrue(scc.__contains__([NodeData(4), NodeData(3)]))

    def test_plot_graph(self):
        algo = GraphAlgo()
        algo.load_from_json('../data/A5')
        algo.plot_graph()
