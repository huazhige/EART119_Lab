# -*- coding: utf-8 -*-
"""
Midterm question 2
    - find the roots for 3 different functions
    -plot each function
"""
import numpy as np
import matplotlib.pyplot as plt

import opt_utils as opt_utils

#==============================================================================
#                                   function def
#==============================================================================

def f1( x):
    return x**5 + 2/5*x**2 - 2

def f2( x):
    return np.exp( -x/10) + x

def f3( x):
   return 10*np.sin( x/4) + 0.1*(x+12)

#==============================================================================
#                                   params
#==============================================================================
xmin, xmax = -10, 10
#starting point
x0 = 5

#==============================================================================
#                                   find roots w/ Secant method
#==============================================================================

root1 = opt_utils.my_Secant( f1, x0, x0+2)
root2 = opt_utils.my_Secant( f2, x0, x0+2)
root3 = opt_utils.my_Secant( f3, 0, 1)

#==============================================================================
#                                   plot
#==============================================================================
a_x = np.linspace( xmin, xmax, 1000)

plt.figure(1)
plt.title( 'root for first equation')
plt.plot( a_x, f1( a_x), 'k', label = 'f(x)=x^5+2/5x^2-2')
plt.plot( root1, f1( root1), 'r*', label = 'root at x=%f'%(root1))
plt.grid( True)
plt.legend( loc = 'upper left')
plt.xlabel( 'x')
plt.ylabel( 'f(x)')
file_out = 'Watson_Midterm2_1.png'
plt.savefig(file_out, dpi = 150)
plt.show()

plt.figure(2)
plt.title( 'root for second equation')
plt.plot( a_x, f2( a_x), 'k', label = 'f(x)=x^5+2/5x^2-2')
plt.plot( root2, f2( root2), 'r*', label = 'root at x=%f'%(root2))
plt.grid( True)
plt.legend( loc = 'upper left')
plt.xlabel( 'x')
plt.ylabel( 'f(x)')
file_out = 'Watson_Midterm2_2.png'
plt.savefig(file_out, dpi = 150)
plt.show()

plt.figure(3)
plt.title( 'root for third equation')
plt.plot( a_x, f3( a_x), 'k', label = 'f(x)=x^5+2/5x^2-2')
plt.plot( root3, f3( root3), 'r*', label = 'root at x=%f'%(root3))
plt.legend( loc = 'upper left')
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'f(x)')
file_out = 'Watson_Midterm2_3.png'
plt.savefig(file_out, dpi = 150)
plt.show()















