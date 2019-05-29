#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as int_utils

# =========================1=============================
#                  Function Definitions
# =======================================================
def fct_f(x):
    f = np.sin(x)
    return f

def fct_g(x):
    g = 2*x*np.exp(x**2)
    return g

def fct_F(x):
    F = np.cos(x)
    return F

def fct_G(x):
    G = (2*np.exp(x**2)) + (4*np.exp(x**2)*(x**2))
    return G

# =========================2=============================
#                      Parameters
# =======================================================
fxmin = 0
fxmax = np.pi

gxmin = 0
gxmax = 1

N = 1000

# =========================3=============================
#                  Numerical Integration
# =======================================================
# exact solution
f_IntExact = fct_F(fxmax) - fct_F(fxmin)
g_IntExact = fct_G(gxmax) - fct_G(gxmin)

# numerical approx
f_IntMid = int_utils.midpoint(fct_f, fxmin, fxmax, N)
g_IntMid = int_utils.midpoint(fct_g, gxmin, gxmax, N)

# compare exact and numerical
print('Exact Integral (f):', f_IntExact)
print('Exact Integral (g):', g_IntExact)
print('Numerical Approximation (Midpoint f):', f_IntMid)
print('Numerical Approximation (Midpoint g):', g_IntMid, '\n')

for curr_n in range(10, 1000, 200):
    f_IntMid = int_utils.midpoint(fct_f, fxmin, fxmax, curr_n)
    g_IntMid = int_utils.midpoint(fct_g, gxmin, gxmax, curr_n)
    print('Increment fdx:', float(fxmax - fxmin)/curr_n)
    print('Increment gdx:', float(gxmax - gxmin)/curr_n)
    print('Exact Integral (f):', f_IntExact)
    print('Exact Integral (g):', g_IntExact)
    print('Numerical Approximation (Midpoint f):', f_IntMid)
    print('Numerical Approximation (Midpoint g):', g_IntMid, '\n')

