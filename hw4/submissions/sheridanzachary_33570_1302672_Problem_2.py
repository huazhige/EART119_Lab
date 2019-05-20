# -*- coding: utf-8 -*-
"""
    -Trying secant method first
"""

import numpy as np
import matplotlib.pyplot as plt

#===================function definitions======================================
def f_fct(t): #f(t)
    return 1.1*(t-2.5)**2

def g_fct(t): #g(t)
    return 5*t+2.5

def main_fct(t): #f(t) - g(t)
    return (1.1*(t-2.5)**2) - (5*t+2.5)

def my_secant(fct, x0, x1, tol=1e-5, N=20): #secant method
    x0 = float(x0)
    x1 = float(x1)
    i  = 0
    while abs(fct(x1)) > tol and i < N:
        dfdx = (fct(x1)-fct(x0))/(x1-x0)
        x2 = x1 - fct(x1)/dfdx
        x0 = x1
        x1 = x2
    if abs(fct(x1)) > tol:
        return np.nan
    else:
        return x1
#==================parameters=================================================
#range of t
tmin = -10
tmax = 10
eps  = 1e-1
a_t = np.linspace(tmin, tmax, 1000)
a_mfct = main_fct(a_t)
a_ffct = f_fct(a_t)

t0   = -5 #starting position
t1   = 5  #starting position for second intersection point
#============finding intersection points======================================
intsctn_Sc1 = my_secant(main_fct, t0, t1)
intsctn_Sc2 = my_secant(main_fct, t1, t1+5)
sel = abs(a_mfct) < eps #IC_2_1 method
#===================plots=====================================================
plt.figure(1)
plt.plot(a_t, f_fct(a_t), 'k-') #function f(t)
plt.plot(a_t, g_fct(a_t), 'r-') #function g(t)
plt.plot([intsctn_Sc1], [f_fct(intsctn_Sc1)], 'b*', ms=14) #intersection point 1
plt.plot([intsctn_Sc2], [f_fct(intsctn_Sc2)], 'b*', ms=14) #intersection point 2
plt.plot([a_t[sel][0]], [a_ffct[sel][0]], 'g*', ms=14) #point 1 using vector method
plt.plot([a_t[sel][1]], [a_ffct[sel][1]], 'g*', ms=14) #point 2 using vector method
plt.plot([tmin, tmax], [0, 0], 'r--')
plt.plot([0, 0], [-50, 175], 'r--')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y')
plt.show()
#==================question answers===========================================
"""
    a) There are two intersection points for
       t:[-10, 10]
    b) Point 1: (0.437, 4.683)
       Point 2: (9.109, 48.044)
    c) See plot. Blue is Secant method and Green 
       is vectorization method.
"""












