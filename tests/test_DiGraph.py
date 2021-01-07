import unittest

from src.DiGraph import DiGraph
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
        self.assertEqual(edges_in.get(2), 1, 'Doesn\'t contain all edges')

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
        self.assertEqual(edges_in.get(2), 1, 'Doesn\'t contain all edges')
        self.assertEqual(edges_in.get(3), 1, 'Doesn\'t contain all edges')

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
        self.assertEqual(8, graph.get_mc())
        graph.remove_node(2)
        self.assertEqual(graph.get_mc(), 11)

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 1)
        self.assertEqual(graph.all_in_edges_of_node(2).get(1), 1, "yalla")
        self.assertEqual(graph.all_out_edges_of_node(1).get(2), 1, "yalla")
        graph.add_edge(1, 2, 1)
        self.assertEqual(graph.all_out_edges_of_node(1).get(2), 1, "failed in add duplicate test")
        self.assertEqual(graph.all_in_edges_of_node(2).get(1), 1, "failed in add duplicate test")
        self.assertEqual(graph.e_size(), 1, "failed in add duplicate test")

        graph.add_edge(1, 1, 1)
        self.assertEqual(graph.all_out_edges_of_node(1).get(1), None, "failed in add duplicate test")
        self.assertEqual(graph.all_in_edges_of_node(1).get(1), None, "failed in add duplicate test")
        self.assertEqual(graph.e_size(), 1, "failed in add duplicate test")

    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(1)
        self.assertEqual(graph.get_node(1), NodeData(1))

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 1)
        self.assertEqual(graph.e_size(), 2)
        self.assertEqual(graph.v_size(), 3)
        graph.remove_node(1)
        self.assertEqual(graph.e_size(), 0)
        self.assertEqual(graph.v_size(), 2)
        self.assertEqual(graph.get_node(1), None)
        self.assertEqual(graph.get_all_v(), {2: NodeData(2), 3: NodeData(3)})

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 1)
        self.assertEqual(graph.all_in_edges_of_node(2).get(1), 1)
        self.assertEqual(graph.all_out_edges_of_node(1).get(2), 1)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.all_in_edges_of_node(2).get(1), None)
        self.assertEqual(graph.all_out_edges_of_node(1).get(2), None)
        self.assertEqual(graph.e_size(), 1)
