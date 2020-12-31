import sys

from src.Location import Location


class NodeData:

    def __init__(self, key: int, pos: () = None):
        self.__key: int = key
        self.__pos: Location = Location()
        self.__pos.set_point(pos)
        # params for algorithms
        self.__parent = None
        self.__type = -1
        self.__dist = sys.maxsize
        self.__visited = False
        self.__index = None
        self.__low_link = None

    def get_pos(self) -> tuple:
        return self.__pos.get_point()

    def set_pos(self, point: str):
        self.__pos.set_point_from_string(point)

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def get_parent(self):
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_type(self) -> int:
        return self.__type

    def set_type(self, type: int):
        self.__type = type

    def get_dist(self) -> float:
        return self.__dist

    def set_dist(self, dist: float):
        self.__dist = dist

    def get_visited(self) -> bool:
        return self.__visited

    def set_visited(self, visited: bool):
        self.__visited = visited

    def get_index(self) -> int:
        return self.__index

    def set_index(self, index: int):
        self.__index = index

    def get_low_link(self) -> int:
        return self.__low_link

    def set_low_link(self, low_link: int):
        self.__low_link = low_link

    def __repr__(self):
        if self.__pos is not None:
            return '{id:' + self.__key.__str__() + ', pos:' + self.__pos.__str__() + '}'
        else:
            return '{id:' + self.__key.__str__() + '}'

    def __eq__(self, other):
        return other.get_dist() == self.__dist and other.get_pos() == self.__pos and other.get_key() == self.__key
