# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:01:57 2019
Homework 4 Problem 4
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt


def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        #print (i, abs( fct( x1)), x_next)
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)
def function_1(x):
    return  -(x**5) + (1/3)*(x**2) + (1/2)
def function_2(x):
    return ((np.cos(x))**2 + 0.1)
def function_3(x):
    return np.sin(x/3) + 0.1*(x+5)
roots_1 = my_Secant(function_1, .7, 2)
roots_2 = my_Secant(function_2, 0, 1)
roots_3 = my_Secant(function_3, -3, 3)
#THE SECOND FUNCTION HAS NO ROOTS COS SQUARED IS ALWAYS POSITIVE
print("root of First Function = ", roots_1)
print("root of Second Function = ", roots_2)
print("root of Third Function = ", roots_3)
