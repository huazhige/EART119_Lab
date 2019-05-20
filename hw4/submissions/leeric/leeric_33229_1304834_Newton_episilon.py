# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:47:12 2019
Modified Newton's Method
Homwork 4 Problem 3
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt


def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivative of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    epsilon = 1e-6
    while abs( fct( xn) )> tol and i < N: # f(x) - f(x+dx) < epsilon
        x_next = xn - fct( xn)/df_dt( xn)
        print (i, abs( fct( xn)), x_next)
        xn = float( x_next)
        i += 1
        if abs(fct(xn) - fct(x_next)) > epsilon:
            break
    if abs( fct( xn) - fct(x_next)) > tol:# no solution found
        return None
    else:
        return float( x_next)
