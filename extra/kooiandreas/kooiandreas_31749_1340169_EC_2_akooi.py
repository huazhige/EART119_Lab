#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:05:35 2019

@author: andreaskooi
"""

#======
# imports
#======

import numpy as np
import integrate_utils as iu


#======
# functions
#======


def get_mean( f_x, xmin, xmax, n=1000):
    """
    """
    # create n random points in x 
    a_xran = np.random.uniform( xmin, xmax, n)
    ############ vectorized version ###########
    #num_inside = a_xran.sum()
    f_fct_mean = np.mean( f_x( a_xran ) )
    return f_fct_mean

def a_fct(x):
    return np.sin(x)

def b_fct(x):
    return 2*x*np.exp(x**2)


#======
# computations
#======

# numerical integrations of the part a and part b functions
integral_a = iu.trapezoidal(a_fct, 0, np.pi, 1000)
integral_b = iu.trapezoidal(b_fct, 0, 1, 1000)

# estimated means for these functions
mean_a = get_mean(a_fct, 0, np.pi)
mean_b = get_mean(b_fct, 0, 1)


#======
# print results
#======

print('Part a.)')
print('The calculated mean of f(x) using 1000 points is: ' + str(mean_a))
print('And the numerical integral is: ' + str(integral_a))
print('Part b.)')
print('The calculated mean of g(x) using 1000 points is: ' + str(mean_b))
print('And the numerical integral is: ' + str(integral_b))



# Console output:
'''
Part a.)
The calculated mean of f(x) using 1000 points is: 0.6381195072242417
And the numerical integral is: 1.9999983550656624
Part b.)
The calculated mean of g(x) using 1000 points is: 1.7502624272207084
And the numerical integral is: 1.7182830209330224
'''
