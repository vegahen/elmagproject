import numpy as np

class Coordinate:
    def __init__(self, x, y, z):
        self.x = np.float64(x)
        self.y = np.float64(y)
        self.z = np.float64(z)
    def print(self, unit):
        print("[{0:.2e} {3}, {1:.2e} {3}, {2:.2e} {3}]".format(self.x, self.y, \
            self.z, unit))

class Position(Coordinate):
    def print(self):
        Coordinate.print(self, "m")

class Momentum(Coordinate):
    def print(self):
        Coordinate.print(self, "kg m/s")

class Field(Coordinate):
    def print(self):
        Coordinate.print(self, "T")

class Particle:
    def __init__(self, m, c, x, y, z, px, py, pz):
        self.m = np.float64(m)
        self.q = np.float64(c)
        self.x = Coordinate(x, y, z)
        self.p = Momentum(px,py, pz)
    def print(self):
        print("x: ({0:.2e} {8}, {1:.2e} {8}, {2:.2e} {8})\nv: ({3:.2e} {9}, \
{4:.2e} {9}, {5:.2e} {9})\nm: {6:.2e} kg\nq: {7:.2e} C".format(self.x.x, \
self.x.y, self.x.z, self.p.x/self.m, self.p.y/self.m, self.p.z/self.m, self.m, \
self.q, 'm', 'm/s'))