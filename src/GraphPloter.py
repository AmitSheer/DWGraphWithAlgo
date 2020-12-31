import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from src.GraphInterface import GraphInterface
from src.Location import Location

min_x: float = float('inf')
min_y: float = float('inf')
max_x: float = float('-inf')
max_y: float = float('-inf')
fig, ax = plt.subplots()


def plotter(graph: GraphInterface):
    global min_x, min_y, max_x, max_y, ax
    for node in graph.get_all_v().values():
        if node.get_pos()[0] > max_x:
            max_x = node.get_pos()[0]
        if node.get_pos()[0] < min_x:
            min_x = node.get_pos()[0]
        if node.get_pos()[1] > max_y:
            max_y = node.get_pos()[1]
        if node.get_pos()[1] < min_y:
            min_y = node.get_pos()[1]

    plt.axis([min_x, max_x, min_y, max_y])
    put_edges(graph)
    put_nodes(graph)
    plt.autoscale(True, 'both')
    plt.show()


def put_edges(graph: GraphInterface):
    for node in graph.get_all_v().values():
        for dest in graph.all_out_edges_of_node(node.get_key()).keys():
            plt.arrow(node.get_pos()[0], node.get_pos()[1],
                      graph.get_all_v().get(dest).get_pos()[0] - node.get_pos()[0],
                      graph.get_all_v().get(dest).get_pos()[1] - node.get_pos()[1],
                      width=node.get_location().distance(graph.get_all_v().get(dest).get_location()) / 500,
                      head_width=3 * node.get_location().distance(graph.get_all_v().get(dest).get_location()) / 100,
                      head_length=6 * node.get_location().distance(graph.get_all_v().get(dest).get_location()) / 100,
                      facecolor='black',
                      length_includes_head=True)


def put_nodes(graph: GraphInterface):
    for node in graph.get_all_v().values():
        plt.plot(node.get_pos()[0], node.get_pos()[1], 'ro')
