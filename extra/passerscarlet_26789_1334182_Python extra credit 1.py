#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
EXTRA CREDIT PROBLEM 1

    -computes the integral of the function f(t) = 3t^2*exp(t^3) 
    via: 
       - trapezoidal method 
       - midpoint method 
    -compares these numerical solutions to the exact solution of the 
    definite integral 
        
    
@author: scarletpasser
"""
import numpy as np

###########################################################################
#                               problem 1
###########################################################################

##### params #####
N    = 100000 #Number of trapazoids/areas of midpoint 
tmin = 0      #lower bound of integration
tmax = np.pi  #upper bound of integration

###### function #######
def f_1(t):
    return 3*(t**2)*(np.exp(t**3))

###### analytic function integration#######

def f_1_exact(t):
    """
    - Done by hand
    - t = pi^3
    """           
    return np.exp(t)-1

f_1_exact = f_1_exact(np.pi**3) #exact integral 

###### trapazoidal integration #######
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

f_1_trap = trapezoidal(f_1, tmin, tmax, N)  #integral via trapezoids

###### midpoint integration #######
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

f_1_mid = midpoint(f_1, tmin, tmax, N) #integral via midpoints 

print 'trapezoid integration:', f_1_trap
print 'midpoint integration:', f_1_mid
print 'analytic integration:', f_1_exact


