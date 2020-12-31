from typing import List

from src import GraphInterface
from src.NodeData import NodeData

global sccList
index = 0


def dfs(curr: NodeData, stack, graph: GraphInterface):
    global index
    curr.set_low_link(index)
    curr.set_index(index)
    curr.set_visited(True)
    stack.append(curr)
    index += 1
    for n in list([graph.get_all_v().get(dest)] for dest in
                  graph.all_out_edges_of_node(curr.get_key())):
        node: NodeData = n.pop()
        if node.get_index() is None:
            dfs(node, stack, graph)
            curr.set_low_link(min(curr.get_low_link(), node.get_low_link()))
        elif node.get_visited():
            curr.set_low_link(min(curr.get_low_link(), node.get_index()))
    if curr.get_low_link() == curr.get_index():
        scc = []
        while len(stack):
            popped_node: NodeData = stack.pop()
            popped_node.set_visited(False)
            scc.append(popped_node)
            if popped_node == curr:
                break
        sccList.append(scc)


def trajan(graph: GraphInterface, node_id: int = None) -> List[list]:
    global index
    global sccList
    index = 0
    sccList = []
    stack = []
    if node_id is None:
        for node in list(graph.get_all_v().values()):
            if node.get_index() is None:
                dfs(node, stack, graph)
    else:
        dfs(graph.get_all_v().get(node_id), stack, graph)
    return sccList

# def tarjan_for_single_node(self, node_id):
