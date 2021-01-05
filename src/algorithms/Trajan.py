from typing import List

from src import GraphInterface
from src.NodeData import NodeData

sccList: List[list] = []
__scc_found = set()
index = 0
# index = 0
#
#
# def _dfs(curr: NodeData, stack, graph: GraphInterface):
#     global index
#     curr.set_low_link(index)
#     curr.set_index(index)
#     curr.set_visited(True)
#     stack.append(curr)
#     index += 1
#     for n in list([graph.get_all_v().get(dest)] for dest in
#                   graph.all_out_edges_of_node(curr.get_key())):
#         node: NodeData = n.pop()
#         if node.get_index() is None:
#             _dfs(node, stack, graph)
#             curr.set_low_link(min(curr.get_low_link(), node.get_low_link()))
#         elif node.get_visited():
#             curr.set_low_link(min(curr.get_low_link(), node.get_index()))
#     if curr.get_low_link() == curr.get_index():
#         scc = []
#         while len(stack):
#             popped_node: NodeData = stack.pop()
#             popped_node.set_visited(False)
#             scc.append(popped_node)
#             if popped_node == curr:
#                 break
#         sccList.append(scc)
#
#
# def _update_node(node: NodeData, stack):
#     global index
#     node.set_low_link(index)
#     node.set_index(index)
#     node.set_visited(True)
#     stack.append(node)
#     index += 1
#
#
# def _dfs_non_recursion(curr: NodeData, stack, graph: GraphInterface):
#     _update_node(curr, stack)
#

# def _check_stack_for_dup(curr_stack: List[int], stack_to_check: List[int], iterations: int, graph: GraphInterface):
#     global sccList
#     scc = []
#     for i in range(iterations):
#         if stack_to_check.__contains__(curr_stack[i]):
#             scc.append(graph.get_all_v().get(curr_stack[i]))
#             __scc_found.add(curr_stack[i])
#         else:
#             graph.get_all_v().get(curr_stack[i]).set_visited_in(False)
#             graph.get_all_v().get(curr_stack[i]).set_visited_global(False)
#     sccList.append(scc)


def _travers(curr: NodeData, graph: GraphInterface):
    check_stack = [curr]
    visited = set()
    visited.add(curr.get_key())
    scc = [curr]
    while len(check_stack):
        n = check_stack.pop()
        for dest in graph.all_out_edges_of_node(n.get_key()):
            if dest not in visited:
                node = graph.get_all_v().get(dest)
                visited.add(node.get_key())
                check_stack.append(node)
    # reverse order of the graph
    check_stack = [curr]
    index = 1
    while len(check_stack) and index <= len(visited):
        n = check_stack.pop()
        for dest in graph.all_in_edges_of_node(n.get_key()):
            node = graph.get_all_v().get(dest)
            if dest in visited and node not in scc:
                index += 1
                check_stack.append(node)
                scc.append(node)
    sccList.append(scc)


def _check_dfs(graph: GraphInterface, node: NodeData):
    global __scc_found, sccList, index
    low_link = {}
    scc = {}
    stack = [node]
    index = 0
    while stack:
        n = stack.pop()
        if n.get_key() not in __scc_found:
            low_link[n] = index
            index += 1
        for dest in graph.all_out_edges_of_node(n.get_key()):
            if dest not in __scc_found:
                stack.append(graph.get_all_v().get(dest))


def trajan(graph: GraphInterface, node_id: int = None) -> List[list]:
    global sccList, __scc_found, index
    index = 0
    sccList = []
    if node_id is None:
        for node in list(graph.get_all_v().values()):
            if node.get_key() not in __scc_found:
                _travers(node, graph)
                # _dfs_non_recursion(node, stack, graph)
    else:
        _travers(graph.get_all_v().get(node_id), graph)
        # _dfs_non_recursion(graph.get_all_v().get(node_id), stack, graph)
    return sccList

# def tarjan_for_single_node(self, node_id):
