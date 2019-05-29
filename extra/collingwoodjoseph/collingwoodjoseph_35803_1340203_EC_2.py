# -*- coding: utf-8 -*-
"""
Extra credit problem 2
"""
import numpy as np

pi = np.pi

#FUNCTION DEFINITIONS
def f_x(x):
    return np.sin(x)

def g_x(x):
    return 2*x*np.exp(x**2)

def F_x(x):
    return (-1)*np.cos(x)

def G_x(x):
    return np.exp(x**2)

#DISCRETIZING THE FUNCTIONS AND CALCULATING THE MEAN
f_x_list = np.linspace(0,pi,1000)
g_x_list = np.linspace(0,1,1000)

f_x_avg = np.mean(f_x_list)
g_x_avg = np.mean(g_x_list)

#CALCULATING THE INTEGRAL ANALYTICALLY
f_x_int = F_x(np.pi) - F_x(0)
g_x_int = G_x(1) - G_x(0)

#COMPARISONS
print('f_x average (0,pi): ' + str(f_x_avg))
print('f_x integrated (0,pi): ' + str(f_x_int))
print('g_x average (0,1): ' + str(g_x_avg))
print('g_x integrated (0,1): ' + str(g_x_int))