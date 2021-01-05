from typing import List
import math
from random import random

from src.Frame import get_frame
from src.GraphInterface import GraphInterface


def circle(g: GraphInterface):
    angle = 2.0 * math.pi / g.v_size()
    for v in g.get_all_v().values():
        x = math.cos(v.get_key() * angle)
        y = math.sin(v.get_key() * angle)
        v.set_pos((x, y, 0))


def center_and_scale(g: GraphInterface, width: float, height: float):
    frame = get_frame(g)
    curr_width = frame[1] - frame[0]
    curr_height = frame[3] - frame[2]
    # scale to right size of box
    scale_x = width / curr_width
    scale_y = height / curr_height
    if scale_x < scale_y:
        temp = scale_x
    else:
        temp = scale_y
    scale = 0.9 * temp
    #  offset for all positions
    center = [frame[1] + frame[0], frame[2] + frame[3]]
    offset = [center[0] / 2.0 * scale, center[0] / 2.0 * scale]
    for v in g.get_all_v().values():
        x = v.get_pos()[0]
        y = v.get_pos()[1]
        v.set_pos((x * scale - offset[0], y * scale - offset[1], 0))
