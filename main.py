import math
import random
import numpy as np
from matplotlib import pyplot as plt
from time import time
import networkx as nx
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def graph_random(seed: int, v_size: int, e_size: int):
    g = DiGraph()
    random.seed(seed)
    pos = np.random.random(size=(v_size, 3))
    for i in range(v_size):
        g.add_node(i, (pos[i][0], pos[i][1], pos[i][2]))
    edges = np.random.randint(1, v_size + 1, size=(e_size, 3))
    for edge in edges:
        g.add_edge(edge[0] - 1, edge[1] - 1, random.random())
    return g


nodes: int = int(math.pow(10, 5))
g = graph_random(1000, nodes, nodes * 3)
algo = GraphAlgo(g)
G = nx.DiGraph()
g = algo.get_graph()
for n in g.get_all_v().values():
    G.add_node(n.get_key())
for n in g.get_all_v():
    for e, w in g.all_out_edges_of_node(n).items():
        G.add_edge(n, e)
t1 = time()
scc = nx.strongly_connected_components(G)
t2 = time()
print(f'nx {t2 - t1}')
t1 = time()
a = algo.connected_components()
t2 = time()
print(f'my {t2 - t1}')


