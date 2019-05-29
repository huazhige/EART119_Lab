# -*- coding: utf-8 -*-
"""
Extra Credit: Numerical Integration

Compute the values of the following definite integrals using Monte Carlo Integration.
Compare your results to the exact solution. (Hint: For the first integral, you have to
perform a coordinate transform from cartesian to polar coordinates to solve the
problem analytically).
a. f(x, y) = (x^2 + y^2)^(1/2); Ω = {(x, y) | (x' + y')^(1/2) ≤ r} , and r = 2
Solve: ∫ f(x, y) dx dy
b. w(x, y) = xy^2; Ω = { x | 0 ≤ x ≤ 2
                         y | 0 ≤ y ≤ 1.5}
Solve: ∫ w(x, y)  dx dy
"""
#==============================================================================
#                   Define fcn, vars
#==============================================================================
import numpy as np

print "This may take a minute..."

thetamin, thetamax = 0, 2*np.pi
rmin, rmax         = 0,2
xmin, xmax         = 0, 2
ymin, ymax         = 0, 1.5
n                  = 1000

def f( r, theta):
    return r**2

def w( x, y):
    return x*y**2

def w_gxy( x, y):
    """-  rectangular domain
    return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
        return f_retVal
    
def f_gxy( r, theta):
    """-  rectangular domain
    return: -1 for points outside
    """
    f_retVal = -1
    if r >= 0 and r <= 2 and theta >= 0 and theta <= 2*np.pi:
        f_retVal = 1
        return f_retVal
    
def f_int( r, theta):
    return 2*np.pi*(r**3)/3

def w_int( x, y):
    return (x**2)*(y**3)/6
#==============================================================================
#                   Define Methods
#==============================================================================
def monteCarlo( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    """
        - integrate fct f_xy over potential complex domain omega described by g(x,y)
          --> g(x,y) has to defined so that pointes within domain follow:
              g(x,y) >= 0
        (1) randomly draw n points in x and y,
        (2) find points in domain g(x,y), which is embeded in a rectangle
            wiht Ar and bounded by (xmin, xmax, ymin, ymax)
        (3) compute mean function values of points inside of domain omega
        (4) compute area of domain omega from fraction of points and Ar
        (5) Int(f_xy dxdy) = f_mean*A_omega
    :param f_xy:  - function that should be integrated
    :param g_xy:  - function that defines integration domain
                    g >= 0
    g_xy is embeded in rectangle with:
    :param  - xmin, xmax, ymin, ymax
    :param n:  - number of random points in x and y, total no. = n**2

    :return: - float( ) - definite integral of f_xy
    """
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ########### solve using for loop: A_om, f_mean###########
    f_fct_mean = 0
    num_inside = 0 # number of points with x,y; g(x,y) >= 0
    for i in range( n): # x loop
        for j in range( n): # y loop
            if g_xy( a_xran[i], a_yran[j]) >= 0:
                num_inside += 1
                f_fct_mean += f_xy( a_xran[i], a_yran[j])
    f_fct_mean /= num_inside
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

#==============================================================================
#                   Calculate, Output
#==============================================================================
f_exact = f_int(rmax, thetamax) - f_int(rmin, thetamin)
w_exact = w_int(xmax, ymax)     - w_int(xmin, ymin)

f_mc = monteCarlo(f, f_gxy, rmin, rmax, thetamin, thetamax, n)    
w_mc = monteCarlo(w, w_gxy, xmin, xmax, ymin, ymax, n)

print '        Monte Carlo:     Exact:'
print 'f(x,y): %3.5f, %15.5f' % (f_mc, f_exact)
print 'w(x,y): %3.5f, %15.5f' % (w_mc, w_exact)