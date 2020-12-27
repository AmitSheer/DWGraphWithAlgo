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