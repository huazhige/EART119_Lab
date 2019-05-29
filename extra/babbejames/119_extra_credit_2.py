#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:01:13 2019

@author: jtbabbe
"""

import numpy as np

#=============================================
#           Fct Def
#=============================================

def f( x):
    return np.sin(x)

def g( y):
    return 2*y*np.exp(y**2)

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
    return dx*f_Int

#=============================================
#           parameters
#=============================================

x = np.linspace(0, np.pi, 1000)
y = np.linspace(0, 1, 1000)

#=============================================
#           mean value
#=============================================

fx = f(x)
gy = g(y)

fx_mean = np.mean(fx)
gy_mean = np.mean(gy)

#=============================================
#           mean value
#=============================================

fx_int = trapezoidal ( f, 0, np.pi, 1000)
gy_int = trapezoidal ( g, 0, 1, 1000)

#=============================================
#           Print
#=============================================

print('f(x): f(x)_mean value = ', round( fx_mean, 4) , ', f(x)_numerical_integral = ', round(fx_int, 4))
print('g(x): g(x)_mean value = ', round( gy_mean, 4) , ', f(x)_numerical_integral = ', round(gy_int, 4))


