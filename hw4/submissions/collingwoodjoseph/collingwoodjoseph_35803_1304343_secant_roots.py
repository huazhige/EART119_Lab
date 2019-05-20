# -*- coding: utf-8 -*-
"""
HOMEWORK 4 QUESTION 4
"""
import math
import opt_utils

def f1_x(x):
    return -(x**5) + x**2*(1.0/3.0) + 0.5

def f2_x(x):
    return math.cos(x)**2 + 0.1

def f3_x(x):
    return math.sin(x/3.0) + 0.1*(x+5)

for x in range(-10,10):
    roots_f1 = opt_utils.my_Secant(f1_x,x,x+.1)
    roots_f2 = opt_utils.my_Secant(f2_x,x,x+.1)
    
for x in range(-3,3):
    roots_f3 = opt_utils.my_Secant(f3_x,x,x+.1)
    
print 'f1 root(-10,10): ' + str(roots_f1)
print 'f2 root(-10,10): ' + str(roots_f2)
print 'f3 root(-3,3): ' + str(roots_f3)