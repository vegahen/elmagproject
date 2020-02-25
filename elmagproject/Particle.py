import numpy as np

class Coordinate:
    def __init__(self, x, y, z):
        self.x = np.float64(x)
        self.y = np.float64(y)
        self.z = np.float64(z)

class Momentum:
    def __init__(self, px, py, pz):
        self.px = np.float64(px)
        self.py = np.float64(py)
        self.pz = np.float64(pz)

class Particle:
    def __init__(self, m, c, x, y, z, px, py, pz):
        self.m = np.float64(m)
        self.q = np.float64(c)
        self.x = Coordinate(x, y, z)
        self.p = Momentum(px,py, pz)
    def print(self):
        print("x: ({0:.2e} m, {1:.2e} m, {2:.2e} m)\nv: ({3:.2e} m/s, {4:.2e} \
m/s, {5:.2e} m/s)\nm: {6:.2e} kg\nq: {7:.2e} C".format(self.x.x, self.x.y, \
self.x.z, self.p.px/self.m, self.p.py/self.m, self.p.pz/self.m, self.m, self.q))