# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import opt_utils as opt_utils

xmin, xmax = -10, 10
x0 = 5

#=============== Define Fct. ===============#
def fct_1( x):
    return x**5 + 2./5*x**2 - 2

def fct_2( x):
    return np.exp(-x/10) + x

def fct_3( x):
    return 10*np.sin( x/4) + 0.1*(x+12)

#=============== Find Roots ===============#
#using secant method from module/ data opt_utils
f_Se_1  = opt_utils.my_Secant( fct_1, x0, x0+10, N = 20)
f_Se_2 = opt_utils.my_Secant( fct_2, x0, x0+10, N = 20)
f_Se_3 = opt_utils.my_Secant( fct_3, x0, x0+10, N = 20)

ax = np.linspace( xmin, xmax, 1000)
plt.plot( ax, fct_1( ax),  'r-', label = 'f1(x)')
plt.plot( ax, fct_2( ax),  'b-', label = 'f2(x)')
plt.plot( ax, fct_3( ax),  'g-', label = 'f3(x)')
plt.plot( [xmin, xmax], [0,0], 'k--')
plt.plot( [f_Se_1], [fct_1( f_Se_1)],   'k*', mfc = 'w', ms = 10) 
plt.plot( [f_Se_2], [fct_2( f_Se_2)],   'r*', mfc = 'w', ms = 10)
#plt.plot( [f_Se_3], [fct_3( f_Se_3)],   'r*', mfc = 'w', ms = 10)   not needed/ does not land ofn the graphs
plt.xlabel( 't')
plt.ylabel( 'Function Values')
plt.ylim( -13, 14)
plt.grid( True)
plt.legend()
plt.savefig( 'Plot_#2')
plt.show()
