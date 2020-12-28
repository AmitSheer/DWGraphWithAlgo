import unittest
from src.DiGraph import DiGraph
from src.EdgeData import EdgeData
from src.NodeData import NodeData


class TestDiGraph(unittest.TestCase):
    def test_v_size(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        assert graph.v_size() == 2, 'count number of nodes incorrectly'
        graph.remove_node(1)
        assert graph.v_size() == 1, 'after delete count number of nodes incorrectly'

    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 2)
        assert graph.e_size() == 1, 'count number of edges incorrectly'
        graph.add_edge(2, 1, 2)
        assert graph.e_size() == 2, 'after adding a new edge, number of edges is incorrect'

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        nodes = graph.get_all_v()
        self.assertEqual(len(nodes.values()), 2, 'not all nodes returned')
        self.assertEqual(nodes.get(1), NodeData(1), 'Doesn\'t contain all nodes')
        self.assertEqual(nodes.get(2), NodeData(2), 'Doesn\'t contain all nodes')

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 1, 1)
        edges_in = graph.all_in_edges_of_node(1)
        self.assertEqual(len(edges_in.values()), 1, 'not all nodes returned')
        self.assertEqual(edges_in.get(2), EdgeData(2, 1, 1), 'Doesn\'t contain all edges')

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 1)
        graph.add_edge(2, 1, 1)
        graph.add_edge(2, 3, 1)
        edges_in = graph.all_out_edges_of_node(1)
        self.assertEqual(len(edges_in.values()), 2, 'not all nodes returned')
        self.assertEqual(edges_in.get(2), EdgeData(1, 2, 1), 'Doesn\'t contain all edges')
        self.assertEqual(edges_in.get(3), EdgeData(1, 3, 1), 'Doesn\'t contain all edges')

    def test_get_mc(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        self.assertEqual(graph.get_mc(), 3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 1)
        graph.add_edge(2, 1, 1)
        graph.add_edge(2, 3, 1)
        self.assertEqual(graph.get_mc(), 7)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.get_mc(), 8)
        graph.remove_node(2)
        self.assertEqual(graph.get_mc(), 8)

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
