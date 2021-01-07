from typing import List, Dict

from src import GraphInterface
from src.NodeData import NodeData

sccList: List[list] = []
__scc_found = set()
index = 0


# recursion version
def _dfs(curr: NodeData, stack, graph: GraphInterface):
    global index
    curr.set_low_link(index)
    curr.set_index(index)
    curr.set_visited_in(True)
    stack.append(curr)
    index += 1
    for n in list([graph.get_all_v().get(dest)] for dest in
                  graph.all_out_edges_of_node(curr.get_key())):
        node: NodeData = n.pop()
        if node.get_index() is None:
            _dfs(node, stack, graph)
            curr.set_low_link(min(curr.get_low_link(), node.get_low_link()))
        elif node.get_visited_in():
            curr.set_low_link(min(curr.get_low_link(), node.get_index()))
    if curr.get_low_link() == curr.get_index():
        scc = []
        while len(stack):
            popped_node: NodeData = stack.pop()
            popped_node.set_visited_in(False)
            scc.append(popped_node)
            if popped_node == curr:
                break
        sccList.append(scc)


# non recursion version
def _dfs_non_recursive(graph: GraphInterface, node, low_link, ids):
    global __scc_found, sccList, index
    stack = [node]
    scc: Dict[int, list] = {}
    nodes = graph.get_all_v()
    while stack:
        node = stack[-1]
        if node not in ids:
            ids[node] = low_link[node] = index
            scc[index] = [nodes[node]]
            index += 1
        recursive = True
        # mimic the behavior of recursion by stopping run on edge when we find an edge to visit
        for dest in graph.all_out_edges_of_node(node):
            if dest not in ids:
                stack.append(dest)
                recursive = False
                break
        # if recursive is true it means we visited all reachable nodes from current head node
        if recursive:
            # update the low for current
            low = low_link[node]
            for dest in graph.all_out_edges_of_node(node):
                if dest not in __scc_found:
                    low_link[node] = min(low_link.__getitem__(node), low_link[dest])
            stack.pop()
            if low_link[node] == ids[node]:
                sccList.append(scc[low_link[node]])
                __scc_found.update([key.get_key() for key in scc[low_link[node]]])
            else:
                if low_link[node] not in scc:
                    scc[low_link[node]] = []
                scc[low_link[node]].extend(scc[low])
                for key in scc[low]:
                    low_link[key.get_key()] = low_link[node]

# finds scc by flipping all edges directions
def kosaraju(curr: int, graph: GraphInterface):
    check_stack = [curr]
    visited = set()
    visited.add(curr)
    scc = [curr]
    while len(check_stack):
        n = check_stack.pop()
        for dest in graph.all_out_edges_of_node(n):
            if dest not in visited:
                visited.add(dest)
                check_stack.append(dest)
    # reverse order of the graph
    check_stack = [curr]
    index = 1
    while len(check_stack) and index <= len(visited):
        n = check_stack.pop()
        for dest in graph.all_in_edges_of_node(n):
            if dest in visited and dest not in scc:
                index += 1
                check_stack.append(dest)
                scc.append(dest)
    return scc


# taken and tried from a website on the internet
def non_recursive(graph: GraphInterface, index, node: int = None):
    global __scc_found, sccList
    ids = {}
    low_link = {}
    if node is None:
        node = list(graph.get_all_v())[0]
    stack = []
    on_stack = {}
    work = [(node, 0)]
    while work:
        # start unpacking all of the list from the end
        # like a stack behavior
        curr, nxt = work[-1]
        # pop the last item in list, mimic  stack behavior
        del work[-1]
        if nxt == 0:
            low_link[curr] = index
            ids[curr] = index
            index += 1
            stack.append(curr)
            on_stack[curr] = True
        recursive = False
        for dest in graph.all_out_edges_of_node(curr):
            if dest not in ids:
                work.append((curr, nxt + 1))
                work.append((dest, 0))
                recursive = True
            elif on_stack[dest]:
                low_link[curr] = min(low_link[curr], ids[dest])
        if recursive:
            continue
        if ids[curr] == low_link[curr]:
            scc = []
            while len(stack):
                dest = stack.pop()
                on_stack[dest] = False
                scc.append(dest)
                if dest == curr:
                    break
            __scc_found.update(scc)
            sccList.append(scc)
        if work:  # NEW: v was recursively visited.
            w = curr
            curr, _ = work[-1]
            low_link[curr] = min(low_link[curr], low_link[w])


def trajan(graph: GraphInterface) -> List[list]:
    global sccList, __scc_found, index
    index = 0
    low_link = {}
    ids = {}
    __scc_found = set()
    sccList = []
    for node in graph.get_all_v():
        if node not in __scc_found:
            _dfs_non_recursive(graph, node, low_link, ids)
    return sccList
