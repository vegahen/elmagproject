#%load_ext autoreload
#%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from common.field import B, Momentum, Field, m_e, q_e, \
    k, r_e, B_uni, plotfield
from common.particle import Coordinate, Particle

x0 = Coordinate(100, 200, 300)      # Corner of a cube with incoming particles

a = B(0, 0, r_e)
b = B(r_e, 0, 0)
a.print()
b.print()

myPart = Particle(m_e, q_e, 1, 2, 3, 10*m_e, 20*m_e, 30*m_e)
myPart.print()

plotfield(B, 7, 1e11, True, -1)

