# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:01:14 2019

@author: Luno Bropez
"""

import numpy as np
from scipy import integrate

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

#Defines the function 
def fx(t):
    return 3 * (t**2) * np.exp(t**3)

#Finds th integral using the trapezoidal method
trap_integral = trapezoidal(fx,0, 1, 1000)
#Finds the integral using the midpoint method
mid_integral = midpoint(fx, 0, 1, 1000)

#Solves for the exact integral os the function, also gives the error
x_ans, err = integrate.quad(fx, 0, 1)

print("Using the trapezoidal method you get %1.10f") % trap_integral
print("Using the midpoint method you get %1.10f") % mid_integral
print("The exact solution is %1.10f and the error is %1.15f") % (x_ans, err)
print("The midpoint method seems to give a closer answer to the actual integral")



