# -*- coding: utf-8 -*-
"""
Extra Credit: Numerical Integration

2. Discretize the following functions between xmin, xmax using N=1000 sample points.
Compute the mean value of the function in the given domain and compare it to the
integral of the function over the same domain. You can compute the integral
numerically or analytically.
a. f(x) = sin(x) ; {0 ≤ x ≤ pi}
b. g(x) = 2xe^x^2; {0 ≤ x ≤ 1} 
"""
#==============================================================================
#                   Define fcn, vars
#==============================================================================
import numpy as np

xmin  = 0
xmaxf = np.pi
xmaxg = 1
N     = 1000

def f(x):
    return np.sin(x)

def g(x):
    return 2*x*np.e**x**2
#==============================================================================
#                   Define Fcns for Int., Avg.
#==============================================================================
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

#Note: can define average as the integral of a fcn over bounds, devided by difference of those bounds
#Therfore, can define avg. as above method over the diffence of bounds
    
def avg_value( fct_x, x0, xn, N):
    """
            Average value of a function using the Midpoint integration method
    :param fct_x:  - function whose average is of interest
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn over difference of xn and x0
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    diff   = xn - x0
    return f_int/diff
#==============================================================================
#                   Calculate, Output
#==============================================================================
fmean = avg_value( f, xmin, xmaxf, N)
gmean = avg_value( g, xmin, xmaxg, N)    

fint  = midpoint( f, xmin, xmaxf, N)
gint  = midpoint( g, xmin, xmaxg, N)
"""
print 'Mean Values'
print '<f(x)>:%4.5f, <g(x)>:%4.5f' %(fmean, gmean)
print 'Integral Values'
print 'F(x):%4.5f, G(x):%4.5f' %(fint, gint)
"""

print         'Mean Values:       Integral Values:'
print '<f(x)>:%4.5f,    F(x):%7.5f' %(fmean, fint)
print '<g(x)>:%4.5f,    G(x):%7.5f' %(gmean, gint)

