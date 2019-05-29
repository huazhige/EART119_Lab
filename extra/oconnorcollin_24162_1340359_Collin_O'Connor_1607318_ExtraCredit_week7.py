# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:26:50 2019

@author: collin O'Connor
"""


import numpy as np
import integrate_utils as int_utils
#==============================================================================
#Question 1
#==============================================================================
"""
Numerical integration of difinite integrals:
ex: f(t) = 3t**2 * exp(t^3)
    F(t) = exp(t^3)
    between: a, b with F'(t) =f(t)
"""

#==============================================================================
#fn defs
#==============================================================================
def fct_f(t):
    return 3*t**2 * np.exp(t**3)

def fct_F(t):
    return np.exp(t**3)

###########integration fn##########
def trapezoidal(fct_x, x0, xn, N):
    """
        composite trapezoidal method
        impelmentation of eq 3.17 pg 60 in Linge & Langtangen
        
    params:
        fct_x = compute integral of the fn.
        x0, xn = integration bounds
        N = number of trapezoids
        
    return: 
        value of definite integral of fct_x
        between x0 and xn
    """
    dx = float(xn-x0)/N
    #wrtite sum as for loop
    f_Integ = 0.5*(fct_x(x0) + fct_x(xn))
    for i in range(1, N):
        f_Integ += fct_x(x0 + i*dx)
    ## write sum in vectorized form
    #f_Integ = 0.5*(fct_x(x0) + fct_x(xn)) + (fct_x(x0 + dx*np.arange(1, N, 1))).sum()
    return dx*f_Integ

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
#parameters
#==============================================================================
xmin, xmax = 0, 1
N = 1000
 
#==============================================================================
#num integration and plotting
#==============================================================================
#exact solution
f_IntExact = fct_F(xmax) - fct_F(xmin)

#Trapazoidal method numerical approximation
f_IntNum = trapezoidal(fct_f, xmin, xmax, N)

#Midpoint method numerical approximation
f_mid=midpoint(fct_f, xmin, xmax, N)

#compare exact and Numerical
print "Question 1:"
print 'exact integral: ', f_IntExact
print 'Trapazoidal Method Numerical approx.: ', f_IntNum
print 'Midpoint Method Numerical approx.: ', f_mid
print

#==============================================================================
#Question 2
#==============================================================================
"""Compute mean value of fns
   and compare to the definite integral:
f(x)=sin(x)
g(x)=2x*exp(x**2)
 """
def fx(x):
    return np.sin(x)

def gx(x):
    return 2*x * np.exp(x**2)

def mean_val(integral_fx, xmax, xmin):
    return (1/(xmax - xmin)) * integral_fx

print "Question 2:"
print 'mean value of f(x): ', round(mean_val(trapezoidal(fx,0, np.pi, 1000), np.pi, 0), 3)
print 'integral of f(x): ', round(trapezoidal(fx,0, np.pi, 1000), 3)
print 'mean value of g(x): ', round(mean_val(trapezoidal(gx, 0, 1, 1000), 1, 0), 3)
print 'Integral of g(x): ', round(trapezoidal(gx, 0, 1, 1000), 3)
print

#==============================================================================
#Question 3
#==============================================================================
#================================================
#          fct definition
#================================================
def fct2_xy( x, y):
    return (x**2 + y**2)**0.5

def fct_xy( x, y):
    return x*(y**2)

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct_Fxy_exact(x, y):
    return (0.5*(x**2))+ ((1./3)*(y**3))

def fct_exact(r, theta):
    return theta*((r**3)/3.)

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

rmin, rmax = 0, 2
theta_min, theta_max = 0, 2*np.pi


#================================================
#          compute integral 
#================================================
#compute definite integral
print "Question 3:"

print ('exact solution part a: ', round(fct_exact(rmax, theta_max) - fct_exact(rmin, theta_min), 3))
print 'monte Carlo solution part a: '
for n in np.arange(100, 1200, 200):
    gInt = int_utils.monteCarlo(fct2_xy, fct_gxy, rmin, rmax, theta_min, theta_max, n)
    #in unt_utils the MonteCarlo method results was supposed to be squared, but they never were.
    gInt = gInt**2 
    print 'no. random points', n, 'number integral', round(gInt, 3)
    
print
    
print('exac. sol part b: ', round(fct_Fxy_exact(xmax, ymax) - fct_Fxy_exact(xmin, ymin), 3))


print 'monte Carlo solution part b: '
for n in np.arange(100, 1200, 200):
    fInt=int_utils.monteCarlo(fct_xy, fct_gxy, xmin+1, xmax+1, ymin, ymax, n )
    #in unt_utils the MonteCarlo method results was supposed to be squared, but they never were.
    fInt = (fInt**2)
    print 'no. random points', n, 'number integral', round(fInt, 3)




