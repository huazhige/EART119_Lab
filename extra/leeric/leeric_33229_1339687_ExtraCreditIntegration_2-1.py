# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:35:20 2019
Problem 2 Extra Credit Integration
Mean Value
@author: eric_
"""
import numpy as np


#===============================================================
#               parameters
#===============================================================
N = 100000 # Number of steps
xmin = 0 
xmax = np.pi

xmin_1 = 0
xmax_1 = 1

#================================================================
#               functions
#================================================================

def sin(x):
    return np.sin(x)
def function_1(x):
    return 2*x*np.exp(x**2)

#================================================================
#               mean value
#================================================================
def mean_value(f_t, xmin, xmax, N) :
    function = 0
    del_x = (xmax - xmin)/N
    for i in range(N):
        xi = xmin + i*del_x
        function += f_t(xi)
    return function/N
mean_sin = mean_value(sin, xmin, xmax, N)
print("Mean Value of sinx from 0 to pi: ", mean_sin)
print("Analytic Answer: ", 2/np.pi)
print("Percent Error: ", ((2/np.pi) - mean_sin)*100, "%")
print()
mean_function_1 = mean_value(function_1, xmin_1, xmax_1, N)
print("Mean Value of 2xe^(x^2) from 0 to 1: ", mean_function_1)
print("Analytic Answer" , np.exp(1) - 1)
print("Percent Error: ", (np.exp(1) - 1 - mean_function_1)*100, "%")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


