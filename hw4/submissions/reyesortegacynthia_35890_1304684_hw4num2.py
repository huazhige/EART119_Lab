# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:10:54 2019

@author: creyesor
"""
import opt_utils
import numpy as np
import matplotlib.pyplot as plt


def fct(t) :
    return (1.1(t-2.5)**2) - (5*t + 2.5) #defining the t function
def df_dt(t) : #defining the derivative of the t function
    return 2.2*(t-2.5) - 5
            
for t in range(-10,10): #range bounds
    opt_utils.my_Newton( fct, df_dt, t, tol = 1e4, N = 20) #N is number of max trials
    t =+1
 
t_1 = 0.4366
t_2 = 9.1088

f_t1 = (1.1(t_1-2.5)**2) - (5*t_1 + 2.5) #plugs in first value into the f function
f_t2 = 2.2*(t_1-2.5) - 5




#intersections = f_func(t)- g_func(t) = 0

#set t min to -10
#set t max to 10
