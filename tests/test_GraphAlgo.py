import os
import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):
    def setUp(self):
        self.graph = DiGraph()
        self.graph_algo = GraphAlgo()

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
        self.fail()

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_reset(self):
        self.fail()

    def test_dijkstra(self):
        self.fail()

    def test_trajan(self):
        self.fail()

    def test_dfs(self):
        self.fail()
