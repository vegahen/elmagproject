#%load_ext autoreload
#%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from common.constants import m_e, q_e, r_e
from common.particle import Position, Particle
from common.field import getB, getB_uni, plotfield

x0 = Position(100, 200, 300)      # Corner of a cube with incoming particles


myPart = Particle(1e3*m_e, q_e, 0*r_e, 0, 0, 1e6, 0, 0)

earth = False
N = int(1.2e6)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = np.zeros(N)
ys = np.zeros(N)
zs = np.zeros(N)
for i in range(N):
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #plotfield(getB_uni, ax, 7, 1e11, earth)
    field = getB_uni(myPart.x.x, myPart.x.y, myPart.x.z)
    if i % (N/10) == 0:
        print("Speed: {}".format(np.sqrt(myPart.v.x**2 + myPart.v.y**2 + myPart.v.z**2)))
        print()
        myPart.print()
    myPart.move(field, 1e-9)
    #if myPart.exists or not earth:
    #    ax.scatter(myPart.x.x, myPart.x.y, myPart.x.z, c='red')
    #plt.show()
    xs[i] = myPart.x.x
    ys[i] = myPart.x.y
    zs[i] = myPart.x.z

ax.set_xlim3d(-200, 200)
ax.set_ylim3d(-350, 50)
ax.plot(xs, ys, zs)
plt.show()












