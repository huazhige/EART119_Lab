#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:50:16 2019

@author: andreaskooi
"""
import numpy as np

def my_Newton( fct, df_dt, x0, tol = 1e-6, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    
    xn = float( x0)
    i  = 0
    
        
    print fct( xn + 1) - fct(xn) 
    while abs( fct( xn + 1) - fct(xn) ) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)



'''  for testing purposes


def f_minus_g(t):
    return (1.1*(t - 2.5)**2) - (5*t + 2.5)

def f_minus_g_dt(t):
    return 2.2*(t - 2.5) - 5

intersect = my_Newton(f_minus_g, f_minus_g_dt ,1)
'''

