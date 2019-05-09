# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:42:51 2019

Find roots of following functions
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as scopt

import opt_utils as opt_utils

#===================================================================================
#                                params
#===================================================================================
xmin, xmax = -10, 10

x0 = 1 #first guess
x1 = x0 + 10 #second guess
#===================================================================================
#                                define functions
#===================================================================================
def fct1(x):
    return x**5 + (2/5)*x**2 - 2 

def fct2(x):
    return np.exp(-x/10) + x

def fct3(x):
    return 10*np.sin(x/4) + 0.1*(x+12)

#==================================================================================
#                             find roots
#==================================================================================
    #from opt.utils
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
        print i, abs( fct( x1)), x_next
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)
 #-------------------------------------------------------------------------   
   
 ## solve using secant method
f_Se_x0  = opt_utils.my_Secant( fct1, x0, x0+10, N = 40)
## compare to python solutions:
print( 'secant  ----------- ', f_Se_x0, 'scipy: ', scopt.newton( fct1, x0, fprime = None))

f_Se_x02  = opt_utils.my_Secant( fct2, x0, x0+10, N = 40)
## compare to python solutions:
print( 'secant  ----------- ', f_Se_x0, 'scipy: ', scopt.newton( fct2, x0, fprime = None))

f_Se_x03  = opt_utils.my_Secant( fct3, x0, x0+2, N = 40)
## compare to python solutions:
print( 'secant  ----------- ', f_Se_x03, 'scipy: ', scopt.newton( fct3, x0, fprime = None))

#==================================================================================
#                             plotting
#==================================================================================
a_x = np.linspace( xmin, xmax, 1000) #set x values
plt.plot( a_x, fct1( a_x),  'k-', label = 'f1(x)')
plt.plot( a_x, fct2( a_x),  'g-', label = 'f2(x)')
plt.plot( a_x, fct3( a_x),  'r-', label = 'f3(x)')
plt.plot( [xmin, xmax], [0,0], '--')
plt.plot( [f_Se_x0], [fct1( f_Se_x0)],   'k*', mfc = 'w', ms = 10) #, label = 'Secant')
plt.plot( [f_Se_x02], [fct2( f_Se_x02)],   'g*', mfc = 'w', ms = 10)
plt.plot( [f_Se_x03], [fct3( f_Se_x03)],   'r*', mfc = 'w', ms = 10)
plt.xlabel( 't')
plt.ylabel( 'Function Values')
plt.ylim( -10, 15)
plt.grid( True)
plt.legend()
plt.show()











