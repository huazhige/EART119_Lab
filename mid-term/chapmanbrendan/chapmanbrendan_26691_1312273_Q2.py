# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:24:42 2019

@author: blchapma
"""

#============================================================================
"Packages"
#============================================================================
import numpy as np
import scipy.optimize as scopt
import matplotlib.pyplot as plt
import opt_utils as opt_utils
#----------------------my-func-------------------------------------------

#===================================================================================
#                                params
#===================================================================================
xmin, xmax = -10, 10

x0    = 5
# root finding
tol = 1e-6
iIt = 20
# plotting
tmin, tmax = -10, 15
testPlot = True
#===================================================================================
#                                define fct.
#===================================================================================
def fct1( x):
    return x**5 + 2./5*x**2 - 2

def fct2( x):
    return np.exp( -x/10) + (x)

def fct3( x):
    return 10*(np.sin( x/4)) + 0.1*(x+12)
def my_Secant( fct, par, x0, x1, verbose = False, **kwargs):
    """
    :param fct:     - find root of this fct. closes to x0
    :param par:     - parameters needed for function call: fct( x, par)
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    kwargs:
        :param Nit:       - number of iterations, default = 20
        :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x2
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    N   = 20
    tol = 1e-4
    if 'tol' in kwargs.keys() and kwargs['tol'] is not None:
        tol = kwargs['tol']
    if 'Nit' in kwargs.keys() and kwargs['Nit'] is not None:
        N = kwargs['Nit']
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1, par)) > tol and i < N:
        df_dt  = float(fct( x1,par)-fct( x0,par))/(x1-x0)
        x2 = x1 - fct( x1, par)/df_dt
        if verbose == True:
            print(  i, 'fct-value: ', round( abs( fct( x1, par)),4), 'x: ', round( x2,4))
        # update variables at new step
        x0 = x1
        x1 = x2
        i += 1
    if abs( fct( x1, par)) > tol: # no solution found
        return None
    else:
        return float( x2)
#===================================================================================
#                             find roots
#===================================================================================


## solve using secant method
f_Se_x0  = opt_utils.my_Secant( fct1, x0, x0+10, N = 40)
## compare to python solutions:
print( 'secant  ----------- ', f_Se_x0, 'scipy: ', scopt.newton( fct1, x0, fprime = None))

f_Se_x03  = opt_utils.my_Secant( fct3, x0, x0+2, N = 40)
## compare to python solutions:
print( 'secant  ----------- ', f_Se_x03, 'scipy: ', scopt.newton( fct3, x0, fprime = None))

## test plot
if testPlot == True:
    a_x = np.linspace( xmin, xmax, 1000)
    plt.plot( a_x, fct1( a_x),  'k-', label = 'f1(x)')
    plt.plot( a_x, fct2( a_x),  'g-', label = 'f2(x)')
    plt.plot( a_x, fct3( a_x),  'r-', label = 'f3(x)')
    plt.plot( [xmin, xmax], [0,0], '--')
    plt.plot( [f_Se_x0], [fct1( f_Se_x0)],   'k*', mfc = 'w', ms = 10) #, label = 'Secant')
    plt.plot( [f_Se_x03], [fct3( f_Se_x03)],   'r*', mfc = 'w', ms = 10)
    plt.xlabel( 't')
    plt.ylabel( 'Function Values')
    plt.ylim( -10, 10)
    plt.grid( True)
    plt.legend()
    plt.show()
    
#===================================================================================
    "Image"
#============================================================================


plt.savefig("Q2", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format="PNG",
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()
