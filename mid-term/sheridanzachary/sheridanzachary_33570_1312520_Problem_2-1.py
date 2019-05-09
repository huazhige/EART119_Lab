# -*- coding: utf-8 -*-
"""
    -Problem 2:
        Plotting the three functions given and finding the roots of each 
"""
import numpy as np
import matplotlib.pyplot as plt
#=====================Define Functions========================================
def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    """
    #    - Secant method for solving for roots
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N:
        dfdt = ( fct( x1) - fct(x0))/( x1 - x0)
        x2 = x1 - fct( x1)/dfdt
        
        x0 = x1
        x1 = x2
        
        i += 1
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1

def fct1(x): #function 1: f1(x)
    return x**5. + (2./5.)*x**2. - 2.

def fct2(x): #function 2: f2(x)
    return np.exp(-x/10.) + x

def fct3(x): #function 3: f3(x)
    return 10.*np.sin(x/4.) + 0.1*(x+12)
#======================Parameters=============================================
xmin, xmax = -10, 10
a_x = np.linspace(xmin, xmax, 1001)
x0 = 0
root_1 = my_Secant(fct1, x0+1, x0+1.1)
root_2 = my_Secant(fct2, x0, x0-2)
root_3 = my_Secant(fct3, x0, x0-1)
#=======================Plotting==============================================
plt.figure(1)
plt.plot(a_x, fct1(a_x), 'r-')
plt.plot(a_x, fct2(a_x), 'b-')
plt.plot(a_x, fct3(a_x), 'g-')
plt.plot([0, 0], [-10, 10], 'k--')
plt.plot([-10, 10], [0, 0], 'k--')
plt.plot([root_1], [fct1(root_1)], 'c*', ms=10)
plt.plot([root_2], [fct2(root_2)], 'c*', ms=10)
plt.plot([root_3], [fct3(root_3)], 'c*', ms=10)
plt.ylabel('y')
plt.xlabel('x')
plt.ylim(-10, 10)
plt.grid(True)
plt.show()


