from src.Location import Location


class NodeData:

    def __init__(self, key: int, pos: () = None):
        self.__key: int = key
        self.__pos: Location = Location()
        self.__pos.set_point(pos)
        # params for algorithms
        self.dx = 0
        self.dy = 0
        self.__parent = None
        self.__type = -1
        self.__dist = float('inf')

    #  returns the Location object
    def get_location(self) -> Location:
        return self.__pos

    # return the location as tuple of (x,y,z)
    def get_pos(self) -> tuple:
        return self.__pos.get_point()

    def set_pos(self, point):
        self.__pos.set_point(point)

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

    def __repr__(self):
        if self.__pos is not None:
            return '{id:' + self.__key.__str__() + ', pos:' + self.__pos.__str__() + '}'
        else:
            return '{id:' + self.__key.__str__() + '}'

    def __eq__(self, other):
        return other.get_dist() == self.__dist and other.get_pos() == self.__pos and other.get_key() == self.__key
