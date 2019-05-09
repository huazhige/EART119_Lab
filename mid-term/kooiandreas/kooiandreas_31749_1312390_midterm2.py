#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:31:25 2019

@author: andreaskooi
"""
import numpy as np
import matplotlib.pyplot as plt

#my_Secant taken from opt_utils

#functions

def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x_next
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        #print i, abs( fct( x1)), x_next
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)



def f1(x):
    return x**5 + (2/5)*x**2 - 2
def f2(x):
    return np.exp(-x/10) + x
def f3(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)
    
    


#computations
    
x = np.arange(-10,10,0.1)
dx = 0.2

root1 = my_Secant( f1, 1, 1 + dx)
root2 = my_Secant( f2, 1, 1+ dx)
root3 = my_Secant( f3, 1, 1+ dx)

    
plt.subplot(321)
ax1 = plt.subplot(321)
ax2 = plt.subplot(322)
ax3 = plt.subplot(325)

ax1.plot(x,f1(x), 'r')
ax2.plot(x,f2(x), 'g')
ax3.plot(x,f3(x), 'b')


#plotting

ax1.set_title('Function 1')
ax1.set_xlabel('root at %.2f'%(root1))
ax1.set_ylabel('f(x)')
ax1.legend('root at %.2f'%(root1))
ax2.set_title('Function 2')
ax2.set_xlabel('root at %.2f'%(root2))
ax2.set_ylabel('f(x)')
ax2.legend('root at %.2f'%(root2))
ax3.set_title('Function 3')
ax3.set_xlabel('root at %.2f'%(root3))
ax3.set_ylabel('f(x)')
ax3.legend('root at %.2f'%(root3))


plt.show()

    


