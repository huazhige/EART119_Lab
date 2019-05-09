#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:39:59 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

#initial variables
x0 = 5

#define functions to find roots of
def fct1( x):
    return x**5 + 2./5*x**2 -2

def fct2( x):
    return np.exp( -x/10.) + x

def fct3( x):
    return 10*np.sin( x/4.) + 0.1*(x+12)

#use secant method to find roots of the function
f_Se_x0  = opt_utils.my_Secant( fct1, x0, x0+1, N = 40)
f_Se_x02  = opt_utils.my_Secant( fct2, x0, x0+1, N = 40)
f_Se_x03  = opt_utils.my_Secant( fct3, x0, x0+1, N = 40)

#plot everything
a_x = np.linspace( -10, 10, 1000)
plt.plot( a_x, fct1( a_x),  'k-', label = 'f1(x), root = 1.39630972774')
plt.plot( a_x, fct2( a_x),  'g-', label = 'f2(x), root = -1.1183174318436302')
plt.plot( a_x, fct3( a_x),  'r-', label = 'f3(x), no root in bounds')
plt.plot( [-10, 10], [0,0], '--')
plt.plot( [f_Se_x0], [fct1( f_Se_x0)],   'k*', mfc = 'w', ms = 10) #, label = 'Secant')
plt.plot( [f_Se_x02], [fct2( f_Se_x02)],   'g*', mfc = 'w', ms = 10) #, label = 'Secant')
plt.plot( [f_Se_x03], [fct3( f_Se_x03)],   'r*', mfc = 'w', ms = 10)
plt.xlabel( 'x')
plt.ylabel( 'Function Values')
plt.ylim( -10, 10)
plt.grid( True)
plt.legend()
plt.show()
plt.savefig('Midterm_2_plot.png')