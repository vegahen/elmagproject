import numpy as np

from common.constants import r_e

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
self.x.y, self.x.z, self.v.x, self.v.y/self.m, self.v.z/self.m, self.m, \
self.q, 'm', 'm/s'))

    def move(self, B, dt):
        field = Field(*B(self.x.x, self.x.y, self.x.z))
        a_fac = self.q/self.m
        ax = a_fac * (self.v.y * field.z - self.v.z * field.y)
        ay = a_fac * (self.v.z * field.x - self.v.x * field.z)
        az = a_fac * (self.v.x * field.y - self.v.y * field.x)
        dvx = ax*dt
        dvy = ay*dt
        dvz = az*dt
        dx = dt * (self.v.x + 1/2 * dvx)
        dy = dt * (self.v.y + 1/2 * dvy)
        dz = dt * (self.v.z + 1/2 * dvz)
        self.v.x += dvx
        self.v.y += dvy
        self.v.z += dvz
        self.x.x += dx
        self.x.y += dy
        self.x.z += dz