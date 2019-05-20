# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:13:29 2019
Homework 4 Problem 2
@author: Benny Quiroz
"""
def my_Newton( fct, df_dt, x0, tol = 1e-6, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-6
    :return: f_r0 - closest to x0
    """
    #We're going to do the first iteration outside of the loop that way we can store
    #something in x_last. 
    x_last = float( x0)
    xn = x_last - fct( x_last)/df_dt( x_last)
    i = 0
    #Compares y values and stops if they are too close
    while abs( fct( xn) - fct(x_last)) > tol and i < N: 
        x_last = xn
        xn = x_last - fct( x_last)/df_dt( x_last)
        print (i, abs( fct( x_last)), xn)
        xn = float( xn)
        i += 1
    if abs( fct( xn) - fct(x_last)) > tol:# no solution found
        return None
    else:
        return float( xn)

#Some test code
def f_(t):
    return t**7 - 1000
def compderiv(t):
    return 7*t**6

print(my_Newton(f_, compderiv, 4))
