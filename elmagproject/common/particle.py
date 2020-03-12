import numpy as np

from common.constants import r_e
from common.kutta import RK4

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

class Velocity(Coordinate):
    def print(self):
        Coordinate.print(self, "m/s")

class Field(Coordinate):
    def print(self):
        Coordinate.print(self, "T")

class Particle:
    def __init__(self, m, q, x, y, z, vx, vy, vz):
        self.m = np.float64(m)
        self.q = np.float64(q)
        self.x = Position(x, y, z)
        self.v = Velocity(vx, vy, vz)

    def print(self):
        print("x: ({0:.2e} {8}, {1:.2e} {8}, {2:.2e} {8})\nv: ({3:.2e} {9}, \
{4:.2e} {9}, {5:.2e} {9})\nm: {6:.2e} kg\nq: {7:.2e} C".format(self.x.x, \
self.x.y, self.x.z, self.v.x, self.v.y, self.v.z, self.m, self.q, 'm', 'm/s'))

    def move(self, B, dt, N):
        c = self.q/self.m
        u0 = np.array([self.x.x, self.v.x, self.x.y, self.v.y, self.x.z, self.v.z])
        U = RK4(B, c, u0, dt, N)
        self.x.x = U[N-1][0]
        self.x.y = U[N-1][2]
        self.x.z = U[N-1][4]
        self.v.x = U[N-1][1]
        self.v.y = U[N-1][3]
        self.v.z = U[N-1][5]
        return U
        
