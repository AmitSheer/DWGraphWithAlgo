import heapq
from typing import List

from src import GraphInterface
from src.NodeData import NodeData
import numpy as np


def dijkstra(start: NodeData, key_to_find: int, graph: GraphInterface):
    start.set_dist(0)
    # counter for how many visited
    visited = set()

    # using tuple here so the values won't change
    unvisited_queue = [(start.get_dist(), start.get_key())]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) and len(visited) != graph.v_size():
        current_node: int = heapq.heappop(unvisited_queue)[1]
        if current_node not in visited:
            visited.add(current_node)
            if key_to_find == current_node:
                return
            for dest, w in graph.all_out_edges_of_node(current_node).items():
                if (w + graph.get_all_v().get(current_node).get_dist()) < graph.get_all_v().get(dest).get_dist():
                    graph.get_all_v().get(dest).set_dist(w + graph.get_all_v().get(current_node).get_dist())
                    graph.get_all_v().get(dest).set_parent(current_node)
                    unvisited_queue.append(
                        (graph.get_all_v().get(dest).get_dist(), dest))
            heapq.heapify(unvisited_queue)


def dijkstra_with_arrays(graph: GraphInterface, start: NodeData, key_to_find: int, ):
    Q: set[int] = set()
    dist: List[float] = []
    prev: List = []
    for v in graph.get_all_v():
        dist[v] = float('inf')
        prev[v] = None
        Q.add(v)
    dist[start.get_key()] = 0
    while Q:
        u = np.min(dist)

