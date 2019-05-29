#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
EXTRA CREDIT PROBLEM 3

    - computes the definite integrals of two functions:
        - f(x,y) = (x^2 + y^2)^1/2
        - w(x,y) = xy^2
        using monte Carlo integration over a complex domain
     
    - compares these values to the exact solution of the 
    integrals 

    -WARNING, this program takes a second to run, be patient :)
    
@author: scarletpasser
"""

import numpy as np

###########################################################################
#                            problem 3 part A
###########################################################################

##### params #####

xmin, xmax  = -np.sqrt(2), np.sqrt(2)#bounds of the domain
ymin, ymax  = -np.sqrt(2), np.sqrt(2)

R, theta    = 2, 2*np.pi   #bounds of the domain in polar
n           = 1000         #number of random points used in integration

###### functions #######

def fA( x, y):
    return np.sqrt(x**2 + y**2)

#complex domain
def gA( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal


###### monte carlo integration ######

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

fA_int = monteCarlo( fA, gA, xmin - 1, xmax + 1, ymin - 1, ymax + 1, n)

##### exact solution #####

#converted to polar coordinates and calculated by hand 
def fA_exact(r, theta):
    return (theta*(r**3))/6

fA_exact_int = fA_exact(R, theta)

print 'monteCarlo int (part A):', fA_int
print 'analytic int (part A):', fA_exact_int

###########################################################################
#                           problem 3 Part b
###########################################################################

##### params #####

xmin, xmax = 0, 2       #bounds of the domain 
ymin, ymax = 0, 1.5

###### functions ####### 

def fB( x, y):
    return x*y**2

#complex domain
def gB( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

###### monte carlo integration ######

fB_int = monteCarlo( fB, gB, xmin - 1, xmax + 1, ymin - 1, ymax + 1, n)


##### exact solution #####

#calculated by hand on paper 
def fB_exact(x, y):
    return ((x**2)*(y**3))/6

fB_exact_int = fB_exact(xmax, ymax)

print 'monteCarlo int (part B):', fB_int
print 'analytic int (part B):', fB_exact_int

