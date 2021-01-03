#!/usr/bin/env python
import math
from random import random
from src.DiGraph import DiGraph
from src.Frame import get_frame


def f_a(d, k):
    return d * d / k


# repulsive force
def f_r(d, k):
    return k * k / d


def calculate_repulsive_forces(k, G):
    for v in G.get_all_v().values():
        v.dx = 0
        v.dy = 0
        for u in list(G.get_all_v().values()):
            if v.get_key() != u.get_key():
                dx = v.get_pos()[0] - u.get_pos()[0]
                dy = v.get_pos()[1] - u.get_pos()[1]
                delta = math.sqrt(dx * dx + dy * dy)
                if delta > 0:
                    d = f_r(delta, k) / delta
                    v.dx += dx * d
                    v.dy += dy * d


def calculate_attractive_forces(k, G):
    for edge in G.get_edges():
        v = G.get_node(edge.get_src())
        u = G.get_node(edge.get_dest())
        dx = v.get_pos()[0] - u.get_pos()[0]
        dy = v.get_pos()[1] - u.get_pos()[1]
        delta = math.sqrt(dx * dx + dy * dy)
        if delta > 0:
            d = f_a(delta, k) / delta
            ddx = dx * d
            ddy = dy * d
            v.dx += -ddx
            u.dx += +ddx
            v.dy += -ddy
            u.dy += +ddy


# based on the Fruchterman-Reingold Algorithm but it is catered more for use on graphs with
def fruchterman_reingold(G: DiGraph, iteration=50):
    speed = 1
    area = 1000
    gravity = 20
    # initial position
    frame: tuple = get_frame(G)
    if frame[1] - frame[0] == 0 or frame[3] - frame[2] == 0 or frame == (
            float('inf'), float('-inf'), float('inf'), float('-inf')):
        frame = (-0.1, 1.1, -0.1, 1.1)
    width = abs(frame[1]) - abs(frame[0])
    length = abs(frame[3]) - abs(frame[2])
    area = 10000
    maxDisp = (math.sqrt(100 * area) / 10)
    k = math.sqrt(100 * area) / G.v_size()

    for v in G.get_all_v().values():
        v.get_location().set_x(frame[0] + width * random())
        v.get_location().set_y(frame[2] + length * random())

    print("area:{0}".format(area))
    print("k:{0}".format(k))
    # print("t:{0}, dt:{1}".format(t, dt))

    for i in range(iteration):
        print("iter {0}".format(i))

        # calculate repulsive forces
        calculate_repulsive_forces(k, G)

        # calculate attractive forces
        calculate_attractive_forces(k, G)

        # gravity
        for node in G.get_all_v().values():
            d = math.sqrt(node.dx * node.dx + node.dy * node.dy)
            gf = 0.01 * k * gravity * d
            node.dx -= gf * node.get_location().get_x() / d
            node.dy -= gf * node.get_location().get_y() / d

        # speed
        for node in G.get_all_v().values():
            node.dx *= speed / 800
            node.dy *= speed / 800

        # limit the maximum displacement to the temperature t
        # and then prevent from being displace outside frame
        for v in G.get_all_v().values():
            dx = v.dx
            dy = v.dy
            dist = math.sqrt(dx * dx + dy * dy)
            if dist != 0 and v.get_visited():
                # if dist != 0:
                limitDist = min(maxDisp * (speed / 800), dist)
                v.get_location().set_x((v.get_pos()[0] + dx / dist * limitDist))
                v.get_location().set_y((v.get_pos()[1] + dy / dist * limitDist))
    return G

# def main():
#     graph = DiGraph()
#     for i in range(5):
#         graph.add_node(i)
#     # 0 <-> 1
#     graph.add_edge(0, 1, 1)
#     graph.add_edge(1, 0, 1.1)
#     #  2
#     graph.add_edge(1, 2, 1.3)
#     # 3 <-> 4
#     graph.add_edge(4, 3, 1.1)
#     graph.add_edge(3, 4, 1.1)
#     algo = GraphAlgo()
#     algo.load_from_json('../data/T0.json')
#
#     algo.plot_graph()
