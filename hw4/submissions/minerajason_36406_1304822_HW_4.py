# -*- coding: utf-8 -*-
"""

@author: Jason Minera

#4 find the root of the following functions

F1(x) = -x**5 + 0.333*x**2 + 0.5

F2(x) = cos(x)**2 + 0.1

F3(x) = sin(x/3) + 0.1(x+5)
"""
import opt_utils as ou
import numpy as np


def f1_x(x, verbose = True):
    return -1 * x**5 + 0.333 * x**2 + 0.5

guess = -3

for x in range (-10, 10):
    ou.my_Secant( f1_x, guess, guess + 1, tol = 1e-4)


print("~~~~~~~~~ done F1(x) ~~~~~~~~~~")

#the root is 0.9573 for F1(x)   
  
    
guess = 0
def f2_x(x):
    return np.cos(x)**2 + 0.1

for x in range (-3, 3):
    ou.my_Secant( f2_x, guess, guess + 1, tol = 1e-4)
    
print("~~~~~~~~~ done F2(x) ~~~~~~~~~~")
#no roots were found
    
    
guess =  0 
def f3_x(x):
    return np.sin(x / 3) + 0.1*(x + 5)

for x in range (-10, 10):
    ou.my_Secant( f3_x, guess, guess + 1, tol = 1e-4)
    
print("~~~~~~~~~ done F3(x) ~~~~~~~~~~")
#The root for F3(x) is at x values -1.176
#i tried using verbose to stop the loop from printing every single time but it didnt work