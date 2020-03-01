import numpy as np

m_e = 9.1093837015e-31      # Electron mass [kg]
m_p = 1.67262192369e-27     # Proton mass [kg]
q_e = 1.602176634e-19       # Elementary charge [C]
µ_0 = 1.25663706212e-6      # Vacuum permeability [H/m]
r_e = 6.371e6               # Earth radius [m]
B_0 = 3.12e-5               # Earth's magnetic field at the equator [T]
c = 299792458

mdip = - B_0/µ_0*4*np.pi*r_e**3     # Earth's magnetic dipole moment [A m^2]
kdip = - B_0*r_e**3                 # µ_0 m / 4pi [T m^3]