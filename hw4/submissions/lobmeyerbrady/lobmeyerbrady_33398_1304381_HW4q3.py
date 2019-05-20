# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:19:05 2019

@author: Brady
Homework #3
"""
import numpy as np
import matplotlib.pyplot as plt

def fct(x):
    return -x**2+10*x+9
def dfdx(x):
    return -2*x+10
def my_newton(fct, df_dx, x0):
    """
    -implementation of Newtons's methond for solving f(x) = 0, when f'(x) is known
    """
    xn= float(x0)
    eps = 1e-5
    N=20
    i=0
    while fct(xn+1)-fct(xn)<eps or i<N:
        x_next= xn-fct(xn)/df_dx(xn)
        print( i, 'fct_value', abs(fct( xn)),x_next)
        xn=x_next
        i += 1
    if abs(fct(xn))<eps:    
        return x_next
    else:#solution din not converge
        return np.nan

x0=-9
xmin, xmax= -10, 15
xroot= my_newton(fct, dfdx, x0)


a_x = np.linspace( xmin, xmax, 1000)

plt.figure(1)
plt.plot( a_x, fct(a_x), 'k-')
plt.plot([xroot], [fct(xroot)],'r*', ms = 14 )
plt.plot( [xmin, xmax], [0, 0], 'r--')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Fct values f(x)')
plt.show()






