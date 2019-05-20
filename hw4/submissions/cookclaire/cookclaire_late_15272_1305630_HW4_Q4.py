# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:45:18 2019

"""
import numpy as np
import opt_utils as opt
import math

#=============================part a==========================================
def f1(x):               
    return -x**5 + (1/3)*x**2 + 1/2

f1 = opt.my_Secant( f1, -10, 10)
print f1

#=============================part b==========================================
def f2(x):              
    return math.cos(x)**2 + 0.1

f2 = opt.my_Secant( f2, -10, 10)
print f2

#=============================part c==========================================
def f3(z):               
    return math.sin(z/3) + 0.1*(z + 5)

f3 = opt.my_Secant( f3, -3, 3)
print f3
