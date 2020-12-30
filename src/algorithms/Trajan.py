from typing import List

from src import GraphInterface, NodeData

global sccList
index = 0


def dfs(curr: NodeData, stack, graph: GraphInterface):
    global index
    curr.low_link = index
    curr.index = index
    curr.visited = True
    stack.append(curr)
    curr.index = index
    index += 1
    for n in list([graph.get_all_v().get(edge.dest)] for edge in
                  graph.all_out_edges_of_node(curr.key).values()):
        node = n.pop()
        if node.index is None:
            dfs(node, stack, graph)
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
        sccList.append(scc)


def trajan(graph: GraphInterface, node_id: int = None) -> List[list]:
    global index
    global sccList
    index = 0
    sccList = []
    stack = []
    if node_id is None:
        for node in list(graph.get_all_v().values()):
            if node.index is None:
                dfs(node, stack, graph)
    else:
        dfs(graph.get_all_v().get(node_id), stack, graph)
    return sccList

# def tarjan_for_single_node(self, node_id):
