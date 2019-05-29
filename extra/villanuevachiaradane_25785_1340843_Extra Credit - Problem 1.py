#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as int_utils

# =========================1=============================
#                  Function Definitions
# =======================================================
def fct_f(t):
    f = 3*t**2*np.exp(t**3)
    return f

def fct_F(t):
    F = np.exp(t**3)
    return F

# =========================2=============================
#                      Parameters
# =======================================================
xmin = 0
xmax = 1
N = 10

# =========================3=============================
#                  Numerical Integration
# =======================================================
# exact solution
f_IntExact = fct_F(xmax) - fct_F(xmin)

# numerical approx
f_IntTrap = int_utils.trapezoidal(fct_f, xmin, xmax, N)
f_IntMid = int_utils.midpoint(fct_f, xmin, xmax, N)

# compare exact and numerical
print('Exact Integral:', f_IntExact)
print('Numerical Approximation (Trapezoidal):', f_IntTrap)
print('Numerical Approximation (Midpoint):', f_IntMid, '\n')

for curr_n in range(10, 1000, 200):
    f_IntTrap = int_utils.trapezoidal(fct_f, xmin, xmax, curr_n)
    f_IntMid = int_utils.midpoint(fct_f, xmin, xmax, curr_n)
    print('Increment dx:', float(xmax - xmin)/curr_n)
    print('Exact Integral:', f_IntExact)
    print('Numerical Approximation (Trapezoidal):', f_IntTrap)
    print('Numerical Approximation (Midpoint):', f_IntMid, '\n')

