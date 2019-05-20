#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:25:27 2019
    This function computes the intersection of two functions f(t)
    and g(t).
@author: andrewquartuccio
"""

#=======================================================================================
#                       Imports
#=======================================================================================

import os
import numpy as np
import matplotlib.pyplot as plt

#=======================================================================================
#                       My Imports
#=======================================================================================

import Modules.opt_utils as opt

#=======================================================================================
#                       Parameters
#=======================================================================================

#   Domain setup
N    =  1000
tmin = -10
tmax =  10
t    = np.linspace(tmin, tmax, N-1)

#   Initial Conditions
x0 = -10.0
c  =   1.1
t0 =   2.5
A  =   5.0

#=======================================================================================
#                       Functionsd
#=======================================================================================


#   Functions to find intersections
def f_t(t):
    return 1.1*(t-2.5)**2

def g_t(t):
    return 5.0*t + 2.5

def df_dt(t):
    return 2*1.1*(t-2.5)

#   g(t) derivative is 
def dg_dt():
    return 5.0

#   w(t) = f(t) - g(t)
def w_t(t):
    return (1.1*(t-2.5)**2) - (5.0*t + 2.5)

def dw_dt(t):
    return (2*1.1*(t-2.5)) - 5.0

#   Pass to  my_Newton/my_Secant

point_of_int = opt.my_Newton( w_t, dw_dt, x0, tol = 1e-5, N = 50)

print('The functions intersect at the value t = %.3f') % (point_of_int)
print('The functions intersect 2 times in the interval t=[-10,10].')

a_t  = np.linspace(tmin, tmax, N)
a_ft = f_t(a_t)
a_gt = g_t(a_t)
a_wt = w_t(a_t)

plt.plot(a_t, a_wt, 'ro', ms=2)
plt.plot(a_t, a_ft, 'go', ms=2)
plt.plot(a_t, a_gt, 'bo', ms=2)

dir_out = './Data'
file_out= 'Hw4_2_crossover.png'

os.chdir( dir_out)
plt.savefig( file_out)

plt.show()