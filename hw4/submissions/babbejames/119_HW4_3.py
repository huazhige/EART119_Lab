#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:40:43 2019

HW4: #3

@author: jtbabbe
"""
import numpy as np

#===================================================================
#           parameters
#===================================================================

x0 = -9
# range for independent variables 
xmin, xmax = -10, 15


#===================================================================
#           fct def
#===================================================================

def fct( x):
    return -x**2 + 10*x + 9

def dfdx( x):
    return -2*x + 10

# Modified Newton's method eqn
def my_Newton_modified( fct, df_dx, x0): 
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 0 
    x_diff = 1000
    while x_diff > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        x_diff = abs( fct(xn) - fct(x_next))
        xn = x_next
        i += 1
        print( x_next)
    if abs( x_diff) < eps:        
        return x_next                                   
    else: return np.nan
    
    
    
    
    
def my_Newton_original( fct, df_dx, x0):
    xn = float(x0)
    eps = 1e-5
    N = 20
    i = 0 
    while abs(fct( xn)) > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        print(x_next)
        xn = x_next
        i += 1
    if abs( fct(xn)) < eps:        
        return x_next
    else: return np.nan
    
#===================================================================
#           double check against class example
#===================================================================    

print()
print('Modified Equation')
x_root_modified = my_Newton_modified( fct, dfdx, x0)
print()
print('Unmodified Equation')
x_root_original = my_Newton_original( fct, dfdx, x0)
print()
print( 'Values Match')






