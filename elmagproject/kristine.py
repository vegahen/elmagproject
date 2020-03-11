import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 1, 1001)
f = lambda x : 0*x + 1
y = f(x)

plt.plot(x, f(x))
plt.show()

ns = np.linspace(1, 100, 100, dtype=int)
cs = np.zeros(100)
for n in ns:
    cs[n-1] = 2/np.sinh(n*np.pi)*simps(y*np.sin(n*np.pi*x), dx=x[1]-x[0])

series = np.zeros(1001)

# Endre rangen for å endre hvor mange ledd du har i rekka
for i in range(1):
    series += cs[i]*np.sin(ns[i]*np.pi*x)*np.sinh(ns[i]*np.pi)
    
plt.plot(x, series)
plt.plot(x, y, c='red')
plt.show()



fullseries=np.zeros(1001*1001).reshape(1001, 1001)

u, v = np.mgrid[0:1:1001j, 0:1:1001j]
v
for i in range(100):
    fullseries += cs[i] * np.sin(ns[i]*np.pi*u)*np.sinh(ns[i]*np.pi*v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

y = np.full(1001, 1)
ax.plot(x, y, f(x), c='red')
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)

ax.plot_wireframe(u, v, fullseries, color="blue")

plt.show()