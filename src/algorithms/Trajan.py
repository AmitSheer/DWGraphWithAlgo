from typing import List

from src import GraphInterface
from src.NodeData import NodeData

sccList: List[list] = []
__scc_found = set()
index = 0


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


#
#

def _travers(curr: int, graph: GraphInterface):
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
    __scc_found.update(scc)
    sccList.append(scc)


#
def check_dfs(graph: GraphInterface):
    _sccList = []
    _scc_found = set()
    low_link = {}
    ids = {}
    scc_stack = []
    index = 0
    for node in graph.get_all_v():
        if node not in _scc_found:
            stack = [node]
            while len(stack):
                # start building the stack to run on
                n = stack[len(stack) - 1]
                if n not in ids:
                    index += 1
                    ids[n] = index
                # done represent if we found a node that is already part of an scc in check
                done = True
                for dest in graph.all_out_edges_of_node(n):
                    if dest not in ids:
                        stack.append(dest)
                        done = False
                        break
                if done:
                    low_link[n] = ids[n]
                    # now we start backtracking from current node back
                    for back in graph.all_out_edges_of_node(n):
                        if back not in _scc_found:
                            if ids[back] > ids[n]:
                                low_link[n] = min(low_link.__getitem__(n), low_link[back])
                            else:
                                low_link[n] = min(low_link[n], ids[back])
                    # get rid of the n element in stack
                    stack.pop()
                    # meaning we are at the starting point
                    if low_link[n] == ids[n]:
                        scc = [n]
                        # get the end of the list
                        while scc_stack and ids[scc_stack[len(scc_stack) - 1]] > ids[n]:
                            scc.append(scc_stack.pop())
                        _scc_found.update(scc)
                        _sccList.append(scc)
                    else:
                        scc_stack.append(n)
    return _sccList


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
            low_link[curr] =index
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
                dest = stack[-1]
                del stack[-1]
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

        # n = stack[len(stack) - 1]
        # if n not in ids:
        #     ids[node] = index
        #     index += 1
        # recursion = False
        # for dest in graph.all_out_edges_of_node(n):
        #     # if not in ids means not visited
        #     if dest not in ids:
        #         stack.append(dest)


def trajan(graph: GraphInterface, node_id: int = None) -> List[list]:
    global sccList, __scc_found, index
    index = 0
    low_link = {}
    ids = {}
    __scc_found = set()
    sccList = []
    stack = []
    if node_id is None:
        for node in graph.get_all_v():
            if node not in __scc_found:
                _travers(node, graph)
                # non_recursive(graph, index, node)
                # _dfs(node, stack, graph)
    else:
        # _dfs(graph.get_all_v(graph), stack, graph)
        non_recursive(graph,  index, node_id)
    return sccList
