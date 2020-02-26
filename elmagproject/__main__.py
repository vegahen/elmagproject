import numpy as np
import matplotlib.pyplot as plt
import scipy

from Particle import Particle
from consts import m_e, q_e

myPart = Particle(m_e, q_e, 1, 2, 3, 10*m_e, 20*m_e, 30*m_e)
myPart.print()
type(myPart.q)