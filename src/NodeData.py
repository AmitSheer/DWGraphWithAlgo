import math


class NodeData:

    def __init__(self, key: int, pos: tuple = None):
        self.__key: int = key
        self.__pos = pos
        # params for algorithms
        self.dx = 0
        self.dy = 0
        self.__parent = None
        self.__dist = float('inf')

    # return the location as tuple of (x,y,z)
    def get_pos(self) -> tuple:
        return self.__pos

    def set_pos(self, point: tuple):
        self.__pos = point

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def get_parent(self):
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_dist(self) -> float:
        return self.__dist

    def set_dist(self, dist: float):
        self.__dist = dist

    def distance(self, point) -> float:
        dx = self.__pos[0] - point[0]
        dy = self.__pos[1] - point[1]
        dz = self.__pos[2] - point[2]
        return math.sqrt(dx * dx + dy * dy+dz*dz)

    def __repr__(self):
        if self.__pos is not None:
            return '{id:' + self.__key.__str__() + ', pos:' + self.__pos.__str__() + '}'
        else:
            return '{id:' + self.__key.__str__() + '}'

    def __eq__(self, other):
        return other.get_dist() == self.__dist and other.get_pos() == self.__pos and other.get_key() == self.__key
