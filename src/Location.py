class Location:
    def __init__(self, x: float = None, y: float = None, z: float = None):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def set_point(self, pos: tuple = None):
        if pos is not None:
            self.__x = float(pos[0])
            self.__y = float(pos[1])
            self.__z = float(pos[2])

    def set_point_from_string(self, point: str):
        values = point.split(',')
        self.__x = float(values[0])
        self.__y = float(values[1])
        self.__z = float(values[2])

    def get_point(self):
        if self.__y is None or self.__x is None or self.__z is None:
            return None
        return self.__x, self.__y, self.__z

    def __str__(self):
        return f"({self.__x},{self.__y},{self.__z})"

    def __repr__(self):
        str(self)

    def __eq__(self, other):
        if other is None and self.__x is None and self.__y is None and self.__z is None:
            return True
        return self.__x == other.get_x() and self.__y == other.get_y() and self.__z == other.get_z()