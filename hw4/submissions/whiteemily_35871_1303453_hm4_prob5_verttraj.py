# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:22:45 2019

@author: Emily White

5)      Create three different subplots of position, velocity,
        and acceleration as a fnc of t (save figure)
        Position = z (as a fnc of t)
        Compute velocity (dz/dt)
        Compute acceletation (dz^2/d^2t)
"""
#==============================================================================
#                   modules and import data
#==============================================================================
import numpy as np
import matplotlib.pyplot as plt

file_vertTraj = 'HW4_vertTraj.txt'

#t = time, z = position
Data = np.loadtxt(file_vertTraj, comments = '#').T
t, z = Data[0], Data[1]

#==============================================================================
#                   fnc dfns
#==============================================================================
def fct(t):
    return z

def dz_dt(t):
   return np.gradient(t, z)


def central_diff( fct, dz_dt, t0):
    tn = float(t0)
    eps = 1e-6
    N = 20
    i = 0
    while fct(tn) < eps and i < N:
        t_next = (fct(tn + dz_dt(tn)) - fct(tn - dz_dt(tn)))/ 2*dz_dt(tn)
        print(i, 'fct_value', abs(fct(tn)), t_next) 
        tn = t_next
        i += 1
    if abs(fct(tn)) < eps:
        return t_next
    else: #soln did not converge
        return np.nan

def dz_dt2(t):
    return np.gradient(t, dz_dt)

def central_diff2( fct, dz_dt, t0):
    tn = float(t0)
    eps = 1e-6
    N = 20
    i = 0
    while fct(tn) < eps and i < N:
        t_next = (fct(tn + dz_dt(tn)) - 2*(fct(tn)) + fct(tn - dz_dt(tn)))/ dz_dt(tn)**2
        print(i, 'fct_value', abs(fct(tn)), t_next) 
        tn = t_next
        i += 1
    if abs(fct(tn)) < eps:
        return t_next
    else: #soln did not converge
        return np.nan
#==============================================================================
#                  parameters
#==============================================================================
t0 = -9
tmin, tmax = -10, 10
v_root = central_diff(fct, dz_dt, t0)
a_root = central_diff2(fct, dz_dt2, t0)

#==============================================================================
#                   plots
#==============================================================================
a_t = np.linspace(tmin, tmax, 1000)

plt.figure(1)
plt.plot(a_t, fct(a_t), 'k-')
plt.plot([v_root], [fct(v_root)], 'r*', ms = 14)
plt.plot([a_root], [fct(a_root)], 'b*', ms = 14)
plt.plot([tmin, tmax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Fct values f(x)')
plt.show()









