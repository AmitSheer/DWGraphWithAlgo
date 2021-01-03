from src.GraphInterface import GraphInterface

min_x: float = float('inf')
min_y: float = float('inf')
max_x: float = float('-inf')
max_y: float = float('-inf')


def get_frame(graph: GraphInterface) -> tuple:
    global min_x, min_y, max_x, max_y
    for node in graph.get_all_v().values():
        if node.get_pos() is not None:
            if node.get_pos()[0] > max_x:
                max_x = node.get_pos()[0]
            if node.get_pos()[0] < min_x:
                min_x = node.get_pos()[0]
            if node.get_pos()[1] > max_y:
                max_y = node.get_pos()[1]
            if node.get_pos()[1] < min_y:
                min_y = node.get_pos()[1]
    return min_x, max_x, min_y, max_y
