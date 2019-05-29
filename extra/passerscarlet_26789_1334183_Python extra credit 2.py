#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
EXTRA CREDIT PROBLEM 2

    - computes the mean value of two functions:
        - g(x) from 0 to 1
        - f(x) from 0 to pi
    
    - compares these mean values to the values of the integrals 
    of the functions over the same domain. 
        

@author: scarletpasser
"""

import numpy as np

###########################################################################
#                               problem 2
###########################################################################

##### params #####
fmin = 0     #min value of f function
fmax = np.pi #max value of f function

gmin = 0     #min value of g function
gmax = 1     #max value of g function

N    = 1000  #sample points 

###### functions #######
fx = np.linspace(fmin, fmax, N) #parameters on input 
gx = np.linspace(gmin, gmax, N)

def f(fx):
    return np.sin(fx)

def g(gx):
    return 2*gx*np.exp(gx**2)


###### mean value ######
'''
    - mean = sum of the function over the desired interval 
    divided by the length of that interval 
'''
Mean_f_x = sum(f(fx))*(np.pi/(N))
Mean_g_x = sum(g(gx))/N 


###### midpoint integration ###### 

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

f_int = midpoint(f, fmin, fmax, N)

g_int = midpoint(g, gmin, gmax, N)


print 'mean value of g(x):', Mean_g_x
print 'integration of g(x):', g_int
print 'mean value of f(x):', Mean_f_x
print 'integration of f(x):', f_int


