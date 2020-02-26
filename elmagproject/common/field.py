import numpy as np

from common.particle import Coordinate, Momentum, Particle, Field
from common.constants import m_e, q_e, kdip as k, r_e

B_den = lambda x, y, z : np.sqrt(x**2 + y**2 + z**2)**5
B_x = lambda x, y, z, den: k / den * 3 * x * z
B_y = lambda x, y, z, den: k / den * 3 * y * z
B_z = lambda x, y, z, den: k / den * (2*z**2 - x**2 - y**2)
def B(x, y, z):
    den = B_den(x, y, z)
    return Field(B_x(x, y, z, den), B_y(x, y, z, den), B_z(x, y, z, den))
B_uni = lambda x, y, z : Field(0, 0, k / B_den(r_e, 0, 0) * (-r_e**2))