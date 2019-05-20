#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:26:43 2019

HW4: #4

@author: jtbabbe
"""

import numpy as np
import matplotlib.pyplot as plt

#===================================================================
#           parameters
#===================================================================

x = np.linspace(-10, 10, 1000)
y = np.linspace(-3, 3, 1000)

#===================================================================
#           define functions
#===================================================================

def fx1( x):
    return -x**5 + (1/3)*x**2 + (1/2)

def fx2(x):
    return np.cos(x)**2 + .1

def fy3(y):
    return np.sin(y/3) + .1*(y + 5)
    

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    """
    if dfdx is not known, use secant
    """
    x0 = float( x0)
    x1 = float( x1)
    i=0
    while abs( fct(x1)) > tol and i <N:
        # numerical approx of derivative
        dfdt = (fct( x1) -fct(x0))/(x1-x0)
        # same as Newton's methd
        x_next = x1 - fct(x1)/dfdt
        
        x0 = x1
        x1 = x_next
        
        i += 1
    # check if solution coverged
    if abs(fct(x1)) > tol:
        return np.nan
    else:
        return x1

#===================================================================
#           find roots
#===================================================================

r1 = my_Secant( fx1, -1, 1, tol = .00000001, N = 50)
r2 = my_Secant( fx2, -10, 10, tol = .000001, N = 50)
r3 = my_Secant( fy3, -3, 3, tol = .000001, N = 50)




#===================================================================
#           plot
#===================================================================

plt.figure()
ax1 = plt.subplot(311)
ax1.plot(x, fx1(x))
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

ax2 = plt.subplot(312)
ax2.plot( x, fx2(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

ax3 = plt.subplot(313)
ax3.plot(y, fy3(y))
plt.xlabel('y')
plt.ylabel('f(y)')
plt.grid(True)



#===================================================================
#           Results
#===================================================================
print()
print(' a:', r1) 
print()
print(' b:', r2)
print()
print(' c:', r3)

