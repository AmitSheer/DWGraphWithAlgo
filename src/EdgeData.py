class EdgeData:
    def __init__(self, src: int, dest: int, w: float):
        self.src = src
        self.dest = dest
        self.w = w

    def get_w(self):
        return self.w

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __eq__(self, other):
        return other.get_dest() == self.get_dest() and \
               other.get_src() == self.get_src() and \
               other.get_w() == self.get_w()
