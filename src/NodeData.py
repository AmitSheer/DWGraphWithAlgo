from src.Location import Location


class NodeData:

    def __init__(self, key: int, pos: () = None):
        self.__key: int = key
        self.__pos: Location = Location()
        self.__pos.set_point(pos)
        # params for algorithms
        self.dx = 0
        self.dy = 0
        self.ddx = 0
        self.ddy = 0
        self.__parent = None
        self.__type = -1
        self.__dist = float('inf')
        self.__visited_in = False
        self.__visited_global = False
        self.__index = None
        self.__low_link = None

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

    def get_type(self) -> int:
        return self.__type

    def set_type(self, type: int):
        self.__type = type

    def get_dist(self) -> float:
        return self.__dist

    def set_dist(self, dist: float):
        self.__dist = dist

    def get_visited_in(self) -> bool:
        return self.__visited_in

    def set_visited_in(self, visited: bool):
        self.__visited_in = visited

    def get_visited_global(self) -> bool:
        return self.__visited_global

    def set_visited_global(self, visited: bool):
        self.__visited_global = visited

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
