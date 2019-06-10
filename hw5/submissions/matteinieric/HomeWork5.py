"""
Homework 5 for earth-119 5/20/2019

Intitial value ODE Problem

y'' + (w0**2)*(y) = F * cos(w * t)
"""
# you already know =============================================================
import numpy as np
import matplotlib.pyplot as plt

# Constants ===================================================================
F = 0.5
w0 = 0.8
w = 1

# written solutions a - c ======================================================

"""
a.) y= c1 * np.cos(w0*t) + c2 * np.sin(w0*t) + [F/(w0**2 - w**2)*np.cos(w*t)]

b.) c1 = 25/18
    c2 = 0 

c.) y = 25/18 * (2 * sin(t*[w0 + w]/2) * np.sin(t*[w0 - w]/2))
"""
