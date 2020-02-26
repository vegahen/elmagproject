import numpy as np
import matplotlib.pyplot as plt
import scipy

from common.field import B, Coordinate, Momentum, Particle, Field, m_e, q_e, \
    k, r_e, B_uni

x0 = Coordinate(100, 200, 300)      # Corner of a cube with incoming particles


N = 1

A = np.empty(N, dtype=Particle)
for idx, elem in enumerate(A):
    elem = Particle(m_e, q_e, x0.x, x0.y, x0.z, 0, 0, 0)
    print("Particle number {}".format(idx))
    elem.print()

a = B(0, 0, r_e)
b = B(r_e, 0, 0)
a.print()
b.print()



