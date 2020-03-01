#%load_ext autoreload
#%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from common.constants import m_e, m_p, q_e, r_e, c
from common.particle import Position, Particle, Field
from common.field import getB, getB_uni, plotfield
import common.particle_linear

x0 = Position(100, 200, 300)      # Corner of a cube with incoming particles

"""
field = Field(*getB(r_e, r_e, r_e))
field.print()




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plotfield(getB_uni, ax, 7, 1e11, 3.4*r_e, True)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#plotfield(getB, ax, 7, 1e11, 3.4*r_e, True)
myPart = common.particle_linear.Particle(1e2*m_e, q_e, 0*r_e, 150, 0, 1e7, 0, 1e5)
N = int(1.2e5)
xs = np.zeros(N)
ys = np.zeros(N)
zs = np.zeros(N)
for i in range(N):
    myPart.move(getB_uni, 1e-8)
    xs[i] = myPart.x.x
    ys[i] = myPart.x.y
    zs[i] = myPart.x.z
ax.plot(xs, ys, zs)
plt.show()
plt.plot(xs, ys)
plt.show()
"""



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plotfield(getB, ax, 7, 1e11, 3.4*r_e, True)

n = 1
particles = np.empty(n**2, dtype=Particle)
locs = np.linspace(-r_e, r_e, n)
locs = np.array([r_e])
i = 0
colors = np.array(['red', 'yellow', 'green', 'blue', 'orange'])

for y in locs:
    for z in locs:
        particles[i] = Particle(4*m_p, q_e, -3*r_e, y, z, 5e5, 0, 0)
        i += 1
particles[0].print()
for elem in particles:
    print("once")
    for cols in colors:
        U = elem.move(getB, 3e-3, 10000)
        ax.plot(U[:, 0], U[:, 2], U[:, 4], c=cols)

ax.set_xlim3d(-1.7*r_e, 1.7*r_e)
ax.set_ylim3d(-1.7*r_e, 1.7*r_e)
ax.set_zlim3d(-1.7*r_e, 1.7*r_e)
plt.show()
print(5e5)
print(c*.01)