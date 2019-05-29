# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import integrate_utils as int_utils

#=============================================
#           Fct Def
#=============================================

def fct_f( t):
    return 3*t**2*np.exp(t**3)

def fct_F( t):
    return np.exp( t**3)


def trapezoidal(  fct_x, x0, xn, N):
    dx = float(xn-x0)/N
    f_Int  = 0.5*(fct_x( x0) + fct_x( xn)) + ( fct_x( x0+dx*np.arange(1, N, 1))).sum()
    return dx*f_Int

def midpoint( fct_x, x0, xn, N):
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    return f_int
#=============================================
#           Fct Def
#=============================================

xmin, xmax = 0, 1
N          = 1000

#=============================================
#           Compute Integrals
#=============================================

# exact answer
f_IntExact = fct_F(xmax) - fct_F(xmin)

# numerical answers
f_Int_trapezoid = trapezoidal(fct_f, xmin, xmax, N)
f_Int_midpoint = midpoint(fct_f, xmin, xmax, N)

#=============================================
#           Print
#=============================================

print()
print('Exact Answer: = ', round(f_IntExact, 5))
print()
print('Trapezoidal Method: = ', round(f_Int_trapezoid, 5))
print()
print('Midpoint Method: = ', round(f_Int_midpoint, 5))


