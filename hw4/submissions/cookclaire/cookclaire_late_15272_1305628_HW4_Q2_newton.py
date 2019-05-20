# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:12:11 2019


"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

import opt_utils as opt
#===================================================================================
#                             Parameters
#===================================================================================
t0 = 2.5
c  = 1.1
A  = 5
t = np.arange(-10, 11)

def f(t):                #define functions
    return c*(t - t0)**2 

def g(t):
    return A*t + t0

def F(t):
    return f(t) - g(t)  
print F(t)

#===================================================================================
#                        computation
#===================================================================================
'''
#from sympy import Symbol
t = Symbol ('x')

Ft_dt = sym.diff( F(t), t) #derive the function
print Ft_dt
'''

def Ftdt(t):
     return 2.2*t - 10.5
print Ftdt(t)

CO1 = opt.my_Newton( F, Ftdt, 0) #find cross over points using Newton method
CO2 = opt.my_Newton( F, Ftdt, 9)

print CO1 #first crossover point at approx (0.4366, 4.375)
print CO2 # second crossover at approx (9.1088, )

plt.plot(t, f(t), 'r', label = "f(t)") #plotting f(t) and g(t) show 2 crossover points
plt.plot(t, g(t), 'k', label = "g(t)")
#plt.plot(t, F(t), 'b', label = "F(t)")
plt.legend()
    
    















