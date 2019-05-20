#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:18:59 2019

@author: taylorduncan
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils


#defining function f(t) - g(t) and derivative function f'(t) - g'(t)

def fct(t):
    return (1.1*(t-2.5)**2) - (5*t + 2.5)

def df_dt(t):
    return 2.2*(t-2.5) - 5

#applying newton's method to find crossover points
for t in range(-10,10):
    opt_utils.my_Newton(fct, df_dt ,t, tol = 1e-4, N = 20)
    t +=1
#needed outputs of my_Newton
t_1 = 0.4366
t_2 = 9.1088

#function values for t_1 and t_2
f_t1 = (1.1*(t_1-2.5)**2)
g_t1 = (5*t_1 + 2.5)

f_t2 = (1.1*(t_2-2.5)**2)
g_t2 = (5*t_2 + 2.5)

print f_t1, g_t1, f_t2, g_t2

#ANSWERS TO A AND B
# two crossover points in [-10,10]
# t = 0.4366, 9.1088
# f(.4366), g(.4366) = 4.68338, 4.683
# f(9.1088), g(9.1088) = 48.0438, 48.044