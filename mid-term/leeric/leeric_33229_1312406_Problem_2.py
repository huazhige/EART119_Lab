# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:46:17 2019
Problem 2
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt

#defining functions
def function_1(x):
    return x**5 + (2/5)*x**2 -2
def derivative_1(x):
    return 5*x**4 +(4/5)*x

def function_2(x):
    return np.exp(-x/10) + x
def derivative_2(x):
    return (-1/10)*np.exp(-x/10) + 1

def function_3(x):
    return 10*np.sin(x/4) + 0.1(x + 12)

def derivative_3(x):
    return (2.5)*np.cos(x/4) + 0.1

#newton's Method
def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        #print (i, abs( fct( xn)), x_next)
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)
    
xmin, xmax = -10, 10
time_array = np.linspace(xmin, xmax, 1000)

x_roots_1 = my_Newton(function_1, derivative_1, 1)  

plt.figure(1)
plt.plot(time_array, function_1(time_array), 'k--', label = 'Function 1 x = %f'%x_roots_1)
plt.plot([x_roots_1], [0], 'ro')
plt.grid(True)
plt.legend(loc = 'upper right')

x_roots_2 = my_Newton(function_2, derivative_2, 1)

plt.figure(2)
plt.plot(time_array, function_2(time_array), 'k--', label = 'Function 2 x = %f'%x_roots_2)
plt.plot([x_roots_2], [0], 'ro')
plt.grid(True)
plt.legend(loc = 'upper right')


x_roots_3 = my_Newton(function_3, derivative_3, 1)
plt.figure(3)
plt.plot(time_array, function_3(time_array), 'k--', label = 'Function 3 x = %f'%x_roots_3)
plt.plot([x_roots_3], [0], 'ro')
plt.grid(True)
plt.legend(loc = 'upper right')
    


















