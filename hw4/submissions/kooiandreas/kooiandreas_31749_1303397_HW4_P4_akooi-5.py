#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:01:06 2019

@author: andreaskooi
"""
import numpy as np
import opt_utils as ou

def f1(x):
    return (-x**5) + ((x**2)/3) + 0.5

def f2(x):
    return np.cos(x)**2 + 0.1
    
def f3(x):
    return np.sin(x/3) + 0.1*(x + 5)




dx = 0.1

print("f1(t) has a root at ", ou.my_Secant(f1, 1, 1 + dx) )

print("f2(t) has a root at ", ou.my_Secant(f2, 1, 1 + dx) )

print("f3(t) has a root at ", ou.my_Secant(f3, -1, 1 + dx) )


# Values
# a. )    0.957
# b. )    n/a
# c. )    -1.17