import math
import random
from time import time
from typing import List, Generator
import networkx as nx
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo, json


def graph_random(seed: int, v_size: int, e_size: int):
    g = DiGraph()
    random.seed(seed)
    pos = [(random.random(), random.random(), random.random())] * v_size
    for i in range(v_size):
        g.add_node(i, (pos[i][0], pos[i][1], pos[i][2]))
    while g.e_size() != e_size:
        g.add_edge(random.randint(0, v_size), random.randint(0, v_size), random.random())
    return g


def copy_graph(g, G):
    G.clear()
    for n in g.get_all_v().values():
        G.add_node(n.get_key())
    for n in g.get_all_v():
        for e, w in g.all_out_edges_of_node(n).items():
            G.add_edge(n, e, weight=w)


def compare_scc(scc_nx: set, scc_alg: List[list]):
    a_scc = []
    for s in scc_alg:
        a_scc.append(sorted([node.get_key() for node in s]))
    for c in scc_nx:
        if sorted(list(c)) not in a_scc:
            return False
    return True


def compare_shortest_path(nx_shortest_path, algo_shortest_path):
    return nx_shortest_path[0] == algo_shortest_path[0] and nx_shortest_path[1] == algo_shortest_path[1]


def compare_connected_component(nx_connected_component: Generator, algo_connected_component):
    return sorted([node.get_key() for node in algo_connected_component]) == sorted(
        list(list(nx_connected_component)[0]))


graphs = [
    'G_10_80_0.json', 'G_100_800_0.json', 'G_1000_8000_0.json',
    'G_10000_80000_0.json', 'G_20000_160000_0.json',
    'G_30000_240000_0.json']
results = {}
algo = GraphAlgo()
# for graph in graphs:
#     algo.load_from_json('Graphs_no_pos/' + graph)
# #     # algo.plot_graph()
# #     results[graph] = {}
#     G = nx.DiGraph()
#     copy_graph(algo.get_graph(), G)
#     print(graph, nx.number_strongly_connected_components(G))
for graph in graphs:
    algo.load_from_json('Graphs_no_pos/' + graph)
    results[graph] = {}
    G = nx.DiGraph()
    copy_graph(algo.get_graph(), G)
    # shortest path
    nx_t1 = time()
    nx_shortest_path = nx.single_source_dijkstra(G, 1, 5, weight='weight')
    nx_t2 = time()
    results[graph]['nx_shortest_path'] = float(nx_t2 - nx_t1)
    algo_t1 = time()
    algo_shortest_path = algo.shortest_path(1, 5)
    algo_t2 = time()
    results[graph]['algo_shortest_path'] = float(algo_t2 - algo_t1)
    results[graph]['shortest_path'] = compare_shortest_path(nx_shortest_path, algo_shortest_path)
    #   connected component
    # nx_t1 = time()
    # nx_connected_component = nx.kosaraju_strongly_connected_components(G, 1)
    # nx_t2 = time()
    # results[graph]['nx_connected_component'] = float(nx_t2 - nx_t1)
    algo_t1 = time()
    algo_connected_component = algo.connected_component(1)
    algo_t2 = time()
    results[graph]['algo_connected_component'] = float(algo_t2 - algo_t1)
    # results[graph]['connected_component'] = compare_connected_component(nx_connected_component,
    #                                                                     algo_connected_component)
    #   connected components
    nx_t1 = time()
    nx_connected_components = nx.strongly_connected_components(G)
    nx_t2 = time()
    results[graph]['nx_connected_components'] = float(nx_t2 - nx_t1)
    algo_t1 = time()
    algo_connected_components = algo.connected_components()
    algo_t2 = time()
    results[graph]['algo_connected_components'] = float(algo_t2 - algo_t1)
    results[graph]['connected_components'] = compare_scc(nx_connected_components, algo_connected_components)
with open('results.json', 'w') as json_file:
    json.dump(results, json_file)
