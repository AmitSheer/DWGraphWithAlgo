import heapq

from src import GraphInterface
from src.NodeData import NodeData


def dijkstra(start: NodeData, key_to_find: int, graph: GraphInterface):
    start.set_dist(0)
    # counter for how many visited
    visited = 0

    # using tuple here so the values won change
    unvisited_queue = [(start.get_dist(), start)]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) and visited != graph.v_size():
        current_node: NodeData = heapq.heappop(unvisited_queue)[1]
        if current_node.get_visited() is False:
            current_node.set_visited(True)
            if key_to_find == current_node.get_key():
                return
            for edge in graph.all_out_edges_of_node(current_node.get_key()).values():
                if (edge.get_w() + current_node.get_dist()) < graph.get_all_v().get(edge.get_dest()).get_dist():
                    graph.get_all_v().get(edge.get_dest()).set_dist(edge.get_w() + current_node.get_dist())
                    graph.get_all_v().get(edge.get_dest()).set_parent(current_node)
                    unvisited_queue.append(
                        (graph.get_all_v().get(edge.get_dest()).get_dist(), graph.get_all_v().get(edge.get_dest())))
            heapq.heapify(unvisited_queue)
