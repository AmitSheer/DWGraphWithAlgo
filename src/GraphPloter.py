import math
import threading

import matplotlib.pyplot as plt

from src.Frame import get_frame
from src.GraphInterface import GraphInterface

frame = ()
dist = 0


def put_edges(graph: GraphInterface):
    global dist
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
        plt.plot(node.get_pos()[0], node.get_pos()[1], 'ro', label='Inline label')
        plt.annotate(node.get_key(), (node.get_pos()[0], node.get_pos()[1]), color='blue', fontsize=14)


def plotter(graph: GraphInterface):
    global frame, dist
    frame = get_frame(graph)
    if frame[1] - frame[0] == 0 or frame[3] - frame[2] == 0 or frame == (
            float('inf'), float('-inf'), float('inf'), float('-inf')):
        frame = (-0.1, 1.1, -0.1, 1.1)
    # dist = math.sqrt(math.pow(frame[0] - frame[1], 2) + math.pow(frame[2] - frame[3], 2))
    plt.axis([frame[0], frame[1], frame[2], frame[3]])
    put_nodes(graph)
    put_edges(graph)
    plt.autoscale(True, 'both')
    plt.show()
