# -*- coding: utf-8 -*-
"""
Extra Credit: Numerical Integration

1. Compute the integral of the following function within the given domain. Use both
midpoint and trapezoidal methods! Compare your results to the exact solution of the
definite integral.
a. f(t) = (3t^2)*(e^t^3); {0 ≤ t ≤ 1}

Note: Exact solution =~ 1.88344
"""
import numpy as np
#==============================================================================
#                   Define fcn, vars
#==============================================================================
tmin = 0
tmax = 1
N    = 1000

def f(t):
    return (3*t**2)*(np.e**t**2)

exact = 1.883445123827796
#==============================================================================
#                   Define Int. Methods
#==============================================================================

def trapezoidal(  fct_x, x0, xn, N):
    """
            Composite Trapezoidal Method, eq. 3.17 page 60 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx = float(xn-x0)/N
    # compute intergral: eq. 3.17 page 60 in Linge & Langtangen
    f_Int  = 0.5*(fct_x( x0) + fct_x( xn)) + ( fct_x( x0+dx*np.arange(1, N, 1))).sum()
    # # as a for loop
    # f_Int  = 0.5*(fct_x( x0) + fct_x( xn))
    # for i in range( 1, N):
    #     f_Int += fct_x( x0 + i*dx)
    # print( f_Int*dx)
    return dx*f_Int

def midpoint( fct_x, x0, xn, N):
    """
            Composite Midpoint method, eq. 3.21 page 66 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    return f_int
#==============================================================================
#                   Integrate, Output
#==============================================================================
Trap = trapezoidal( f, tmin, tmax, N)
Mid  = midpoint( f, tmin, tmax, N) 

print 'Trapezoidal result:%8.5f' %(Trap)
print 'Midpoint result:%11.5f' %(Mid)
print 'Exact Solution:%12.5f' %(exact)
