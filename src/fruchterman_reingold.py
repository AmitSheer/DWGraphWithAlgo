import math

from src.GraphInterface import GraphInterface
import numpy as np


def fruchterman_reingold(g: GraphInterface):
    k = 15
    # math.sqrt(1 / (g.v_size()))
    t = math.sqrt(g.v_size())
    k_sqed = k * k
    # repulsion force
    # push the two nodes from each other
    nodes = []
    for v in g.get_all_v().values():
        # Repulsion Force
        for u in g.get_all_v().values():
            if v != u:
                delta = [v.get_pos()[0] - u.get_pos()[0], v.get_pos()[1] - u.get_pos()[1]]
                dist = np.linalg.norm(delta)
                if dist <= 1000 and nodes.__contains__(u.get_key()) is False:
                    rep = k_sqed / dist
                    v.dx += delta[0] / dist * rep
                    u.dx -= delta[0] / dist * rep
                    v.dy += delta[1] / dist * rep
                    u.dy -= delta[1] / dist * rep
        #  Attraction Force
        for e in g.all_out_edges_of_node(v.get_key()):
            u = g.get_all_v().get(e)
            delta = [v.get_pos()[0] - u.get_pos()[0], v.get_pos()[1] - u.get_pos()[1]]
            dist = np.linalg.norm(delta)
            if dist == 0:
                continue
            att = dist * dist / k
            v.dx -= delta[0] / dist * att
            u.dx += delta[0] / dist * att
            v.dy -= delta[1] / dist * att
            u.dy += delta[1] / dist * att
        nodes.append(v.get_key())

    # attraction force
    # every two nodes that are connected to each other are attracted to each other
    # for v in g.get_all_v().values():


    for v in g.get_all_v().values():
        displacement_norm = np.linalg.norm([v.dx, v.dy])
        if displacement_norm < 1:
            continue
        capped_norm = min(t, displacement_norm)
        capped = [v.dx / displacement_norm * capped_norm, v.dy / displacement_norm * capped_norm]
        x = v.get_pos()[0] + capped[0]
        y = v.get_pos()[1] + capped[1]
        v.set_pos((x, y, 0))

    if t > 1.5:
        t *= 0.85
    else:
        t = 1.5
