import math
import random
import numpy as np
from time import time
import networkx as nx
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def graph_random(seed: int, v_size: int, e_size: int):
    g = DiGraph()
    random.seed(seed)
    pos = [(random.random(), random.random(), random.random())] * v_size
    # np.random.random(size=(v_size, 3))
    for i in range(v_size):
        g.add_node(i, (pos[i][0], pos[i][1], pos[i][2]))
    while g.e_size() != e_size:
        g.add_edge(random.randint(0, v_size), random.randint(0, v_size), random.random())
    return g


# ga = GraphAlgo(DiGraph())
# for i in range(1000):
#     ga.get_graph().add_node(i)
#     ga.get_graph().add_edge(i - 1, i, 1)
#     if i % 10 != 0:
#         ga.get_graph().add_edge(i, i - 1, 1)
# start = time()
# ga.connected_components()
# end = time()
# print(f"{(end - start)}")
# G = nx.DiGraph()
# g = ga.get_graph()
# for n in g.get_all_v().values():
#     G.add_node(n.get_key())
# for n in g.get_all_v():
#     for e, w in g.all_out_edges_of_node(n).items():
#         G.add_edge(n, e)
# t1 = time()
# scc = nx.strongly_connected_components(G)
# t2 = time()
# print(f'nx {t2 - t1}')
nodes: int = int(math.pow(10, 5))
g = graph_random(1000, nodes, nodes * 3)
algo = GraphAlgo(g)
# algo = GraphAlgo()
# algo.load_from_json('test1.json')
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
# print(scc)
# algo.plot_graph()
t1 = time()
a = algo.connected_components()
t2 = time()
print(f'my {t2 - t1}')
# print(a.__eq__(scc))
# flag = True
for c in scc:
    d = [g.get_all_v()[n] for n in c]
    # print(d)
    flag = False
    for n in a:
        if n.__contains__(d[0]):
            flag = True
            for node in d:
                if n.__contains__(node) is False:
                    flag = False
                    print(False)
                    break
    if flag is False:
        break

# print(a)
# print(scc)
