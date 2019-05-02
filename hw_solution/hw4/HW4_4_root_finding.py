#python2.7
"""
    -  fix the code below and submit code and the resulting plot to canvas

"""
import numpy as np
import scipy.optimize as scopt
import matplotlib.pyplot as plt

#----------------------my-func-------------------------------------------
import Optimize.opt_utils as opt_utils
#===================================================================================
#                                params
#===================================================================================
xmin, xmax = -10, 10

x0    = 2
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
    return -x**5 + 1./3*x**2 + .5

def fct2( x):
    return np.cos( x)*np.cos( x) + .1

def fct3( x):
    return np.sin( x/3) + 0.1*(x+5)
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