# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:37:33 2019
find the intersection points of f(t) and g(t)
Homework 4 Problem 2
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as op
#===========================================================
#               parameters
#===========================================================
c = 1.1
A = 5
xmin, xmax = -10, 10
time_array = np.linspace(xmin, xmax, 1000)
t0 = 2.5
x0 = 4 # guess point
#===========================================
#               functions
#===========================================
def f_t(x):
    return c*(x-t0)**2 
def g_t(x):
    return A*x + t0
def fandgfunction(x):
    return c*(x- t0)**2 - (A*x + t0)
a_fandg = fandgfunction(time_array)

def fandg_derivative(x):
    return 2*c*(x - t0) - 2*A
x_roots = op.my_Newton(fandgfunction, fandg_derivative, x0 )


a_x = np.linspace(xmin, xmax, 1000)

plt.figure(1)
plt.plot(time_array, a_fandg, 'k--', label = "f(t) - g(t) Newton's Method")
plt.legend(loc = "upper right")
plt.plot([x_roots], [0], 'ko')
plt.plot()

plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
#only one cross over point in the between x = -10 and x = 10
print("t root: ", x_roots)
print("f(t) at intersection point: ", f_t(x_roots))
print("g(t) at intersection point: ", g_t(x_roots))