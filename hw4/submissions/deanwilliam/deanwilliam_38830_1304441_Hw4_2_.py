#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:38:05 2019

@author: williamdean

HW4 problem 2 finding cross-over point between functions using secant method
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils
t_min = -10
t_max = 12
N = 50
t = np.linspace(t_min, t_max, N)
t0 = 2.5
t1 = 9.1
c = 1.1
A = 5.0

def f_t( t):
    return (c*(t - t0)**2)

def g_t( t):
    return (A*t + 2.5)

def df_dt( t):
    return 2*c*(t - t0)

def dg_dt( t):
    return (A)

def h_t( t): # f_t - g_t
    return ((c*(t - t0)**2) - (A*t + t0))

def dfct_dt( t):
    return (df_dt(t) - dg_dt(t))

t_minroot = opt_utils.my_Newton( h_t, dfct_dt, -10, tol = 1e-5, N = 50)
t_maxroot = opt_utils.my_Newton( h_t, dfct_dt, 10, tol = 1e-5, N = 50)

print('The Functions intersect at the value t= [%.3f, %.3f]') % (t_minroot, t_maxroot)

plt.plot( t, f_t( t), 'k-', ms=2)
plt.plot( t, g_t( t), 'b-', ms=2)
#plt.plot( t, h_t(t), 'go', ms=2)
plt.plot( [t_minroot], [h_t(t_minroot)], 'r*', ms = 14)
plt.plot( [t_maxroot], [h_t(t_maxroot)], 'b*', ms = 10)
plt.plot( [t_min, t_max], [0, 0], 'r--')
plt.grid(True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()