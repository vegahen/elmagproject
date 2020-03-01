import numpy as np

from common.constants import m_e, m_p, q_e

def f(u, B, c):
    Bx, By, Bz = B(u[0], u[2], u[4])
    u1 = c * (u[3] * Bz - u[5] * By)
    u3 = c * (u[5] * Bx - u[1] * Bz)
    u5 = c * (u[1] * By - u[3] * Bx)
    return np.array([u[1], u1, u[3], u3, u[5], u5])

def RK4(B, c, u0, dt, N):
    U = np.zeros(N*u0.shape[0]).reshape(N, u0.shape[0])
    U[0] = u0
    for i in range(N-1):
        F1 = f(U[i], B, c)
        F2 = f(U[i] + dt/2 * F1, B, c)
        F3 = f(U[i] + dt/2 * F2, B, c)
        F4 = f(U[i] + dt * F3, B, c)
        U[i+1] = U[i] + dt/6 * (F1 + 2*F2 + 2*F3 + F4)
    return U