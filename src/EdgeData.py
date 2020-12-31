import json


class EdgeData:
    def __init__(self, src: int, dest: int, w: float):
        self.__src = src
        self.__dest = dest
        self.__w = w
        self.__type = -1

    def get_src(self):
        return self.__src

    def get_dest(self):
        return self.__dest

    def get_w(self):
        return self.__w

    def __repr__(self):
        return "{src:" + self.__src.__str__() + ", dest:" + self.__dest.__str__() + ", w:" + self.__w.__str__() + "}"

    def __eq__(self, other):
        return other.get_dest() == self.__dest and \
               other.get_src() == self.__src and \
               other.get_w() == self.__w
