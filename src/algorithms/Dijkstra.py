import heapq

from src import NodeData, GraphInterface


def dijkstra(start: NodeData, key_to_find: int, graph: GraphInterface):
    start.dist = 0
    # counter for how many visited
    visited = 0

    # using tuple here so the values won change
    unvisited_queue = [(start.dist, start)]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) and visited != graph.v_size():
        current_node = heapq.heappop(unvisited_queue)[1]
        if current_node.visited is False:
            current_node.visited = True
            if key_to_find == current_node.key:
                return
            for edge in graph.all_out_edges_of_node(current_node.key).values():
                if (edge.w + current_node.dist) < graph.get_all_v().get(edge.dest).dist:
                    graph.get_all_v().get(edge.dest).dist = edge.w + current_node.dist
                    graph.get_all_v().get(edge.dest).parent = current_node
                    unvisited_queue.append(
                        (graph.get_all_v().get(edge.dest).dist, graph.get_all_v().get(edge.dest)))
            heapq.heapify(unvisited_queue)
