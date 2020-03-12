#%%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from common.constants import m_e, m_p, q_e, r_e, c
from common.particle import Position, Velocity, Field, Particle
from common.field import getB, getB_uni, plotfield
import common.particle_linear
from matplotlib.patches import Circle

#%% Uniform

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
A = Particle(m_e, -q_e, 0, 0, 0, 5e6, 0, 5e5)
print("Uniform, v before: {0:.2e}".format(np.sqrt(A.v.x**2 + A.v.y**2 + A.v.z**2)))
ax.scatter(A.x.x, A.x.y, A.x.z, c='blue')
ax.quiver(A.x.x, A.x.y, A.x.z, A.v.x*1e-7, A.v.y*1e-7, A.v.z*1e-7, colors='blue', label='Velocity')
U = A.move(getB_uni, 1e-8, 530)
print("v after: {0:.2e}".format(np.sqrt(A.v.x**2 + A.v.y**2 + A.v.z**2)))
ax.scatter(A.x.x, A.x.y, A.x.z, c='blue')
ax.quiver(A.x.x, A.x.y, A.x.z, A.v.x*1e-7, A.v.y*1e-7, A.v.z*1e-7, colors='blue')
ax.plot(U[:, 0], U[:, 2], U[:, 4], c='black', label='Path')

ax.set_xlim3d(-1.2, 1.2)
ax.set_ylim3d(-.2, 2.2)
ax.set_zlim3d(-.2, 2.2)

plt.xticks(np.linspace(-1, 1, 3), np.linspace(-1, 1, 3))
plt.xlabel("$x/m$")
plt.yticks(np.linspace(0, 2, 3), np.linspace(0, 2, 3))
plt.ylabel("$y/m$")
ax.set_zticks(np.linspace(0, 2, 3))
ax.set_zticklabels(np.linspace(0, 2, 3))
ax.set_zlabel("$z/m$")

ax.legend()
plt.savefig("uniform.pdf")
plt.show()


#%% Detailed spirals

# Positions
P = np.array([  Particle(4*m_p, 2*q_e,  -10*r_e,    0,      r_e,    3e5,    0,      4e5     ),
                Particle(4*m_p, 2*q_e,  -10*r_e,    3.5e5,  r_e,    5e5,    0,      0       )])     #2

# Parameters
A = np.array([  1e-2,   1.05e3,
                1e-2,   .6e4]).reshape(2, 2)


# Length of axes in 3D plots
L = np.array([  3/5*r_e,      #1
                3/5*r_e])     #2

for i in range(len(P)):
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(111, projection='3d')
    x0 = P[i].x.x
    y0 = P[i].x.y
    z0 = P[i].x.z
    ax.scatter(P[i].x.x, P[i].x.y, P[i].x.z, c='blue')
    ax.quiver(P[i].x.x, P[i].x.y, P[i].x.z, P[i].v.x*2e0, P[i].v.y*2e0, P[i].v.z*2e0, colors='blue', label='Velocity')
    print("Spiral {0}, v before: {1:.2e}".format(i, np.sqrt(P[i].v.x**2 + P[i].v.y**2 + P[i].v.z**2)))
    U = P[i].move(getB, A[i][0], int(A[i][1]))
    print("v after: {0:.2e}".format(np.sqrt(P[i].v.x**2 + P[i].v.y**2 + P[i].v.z**2)))
    ax.scatter(P[i].x.x, P[i].x.y, P[i].x.z, c='blue')
    ax.quiver(P[i].x.x, P[i].x.y, P[i].x.z, P[i].v.x*2e0, P[i].v.y*2e0, P[i].v.z*2e0, colors='blue')
    ax.plot(U[:, 0], U[:, 2], U[:, 4], c='black', label='Path')

    d = L[i]/2
    ax.set_xlim3d(x0-2/5*d, x0+8/5*d)
    ax.set_ylim3d(y0-d, y0+d)
    ax.set_zlim3d(z0-1/5*d, z0+9/5*d)
    
    plt.xticks(np.linspace(-10*r_e, -9.6*r_e, 3), np.linspace(-10, -9.6, 3))
    plt.xlabel("$x/R$")
    plt.yticks(np.linspace(-.2*r_e, .2*r_e, 3), np.linspace(-.4, .4, 3))
    plt.ylabel("$y/R$")
    ax.set_zticks(np.linspace(r_e, 1.4*r_e, 3))
    ax.set_zticklabels(np.linspace(1, 1.4, 3))
    ax.set_zlabel("$z/R$")

    ax.legend()
    plt.savefig("figure{}.pdf".format(i))
    plt.show()

#%% Oscillations

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
B = P[1]
x0 = B.x.x
y0 = B.x.y
z0 = B.x.z
print("Oscillations, v before: {0:.2e}".format(np.sqrt(B.v.x**2 + B.v.y**2 + B.v.z**2)))
U = B.move(getB, 1e-2, int(4.4e5))
print("v after: {0:.2e}".format(np.sqrt(B.v.x**2 + B.v.y**2 + B.v.z**2)))
ax.plot(U[:, 0], U[:, 2], U[:, 4], c='black', label='Path')
d = 1.5*r_e

ax.set_xlim3d(x0-2/5*d, x0+8/5*d)
ax.set_ylim3d(y0-1/10*d, y0+19/10*d)
ax.set_zlim3d(z0-2.3*d, z0-.3*d)

print(z0/r_e)

plt.xticks(np.linspace(-10*r_e, -8*r_e, 3), np.linspace(-10, -8, 3))
plt.xlabel("$x/R$")
plt.yticks(np.linspace(0*r_e, 2*r_e, 3), np.linspace(0, 2, 3))
plt.ylabel("$y/R$")
ax.set_zticks(np.linspace(-r_e, r_e, 3))
ax.set_zticklabels(np.linspace(-1, 1, 3))
ax.set_zlabel("$z/R$")

ax.legend()
plt.savefig("figure2.pdf")
plt.show()

#%% Plot field

xhalfint = 10
xhalfdist = xhalfint*r_e
zhalfint = 10
zhalfdist = zhalfint*r_e

z, x = np.mgrid[-zhalfdist:zhalfdist:101j, -xhalfdist:xhalfdist:101j]
Bx, By, Bz = getB(x, 0, z)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.streamplot(x[0], x[0], Bx, Bz, color='black')
ax.add_artist(Circle((0,0), r_e, color='black'))
plt.xticks(np.linspace(-xhalfdist, xhalfdist, xhalfint+1), np.linspace(-xhalfint, xhalfint, xhalfint+1, dtype=int))
plt.yticks(np.linspace(-zhalfdist, zhalfdist, zhalfint+1), np.linspace(-zhalfint, zhalfint, zhalfint+1, dtype=int))
plt.xlabel('$x/R$')
plt.ylabel('$z/R$')
ax.set_ylim(-5*r_e, 5*r_e)
ax.set_aspect('equal')
fig.savefig('field.pdf')
fig.show()

#%%