# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:55:33 2019

@author: creyesor
"""

import numpy as np
import matplotlib.pyplot as plt

def F1(x):
    return(-x**5) + ((1/3)*x**2) + (1/2) #equation for first func
def F2(x):
    return(cos(x)**2) + 0.1 #equation for second func
    
def F3(x):
    return(sin(x/3) + 0.1*(x+5)) #equation for 3rd func

x0 = -10
x1 = 10
    
for x in range(-10,10):
    opt_utils.my_Secant(F1, x0 + .1, x1) #calculates the secent line in range
    