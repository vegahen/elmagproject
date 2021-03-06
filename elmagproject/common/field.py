import numpy as np

from common.constants import r_e, kdip as k

B_den = lambda x, y, z : np.sqrt(x**2 + y**2 + z**2)**5
B_x = lambda x, y, z, den: k / den * 3 * x * z
B_y = lambda x, y, z, den: k / den * 3 * y * z
B_z = lambda x, y, z, den: k / den * (2*z**2 - x**2 - y**2)
def getB(x, y, z):
    den = B_den(x, y, z)
    return B_x(x, y, z, den), B_y(x, y, z, den), B_z(x, y, z, den)
def getB_uni(x, y, z):
    return 0, 0, k / B_den(r_e, 0, 0) * (-r_e**2)

def plotfield(field, ax, arrows, scale, dist, earth):
    coords = np.linspace(-dist/2, dist/2, arrows)
    for x in coords:
        for y in coords:
            for z in coords:
                if earth and x**2 + y**2 + z**2 < r_e**2:
                    continue
                Bx, By, Bz = field(x, y, z)
                ax.quiver(x, y, z, Bx*scale, By*scale, Bz*scale)