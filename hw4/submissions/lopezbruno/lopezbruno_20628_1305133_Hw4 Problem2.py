# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:21:42 2019

@author: bruno
"""

'''
Finds the crossover point of two functions
this is also the root of the function
'''


#=================Functions============================

import numpy as np
import matplotlib.pyplot as plt



def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)

#This the F(x) function
def ft(t):
     return c * (t - t0)**2
# This is the G(x) function     
def gt(t):
    return A*t + t0
#The derivative of the function
def dfgt(t):
    return A 
#The derivative of the F(x) function
def dfft(t):
    return 2 * c * (t-t0)
    
#F(t) - G(t)
def ht(t):
    return ft(t) - gt(t)
#Derivative of F(t) - G(t)
def dtht(t):
    return dfft(t) - dfgt(t)
#===============Variables=======================================




t0 = 2.5
t1 = 9.1
c = 1.1
A = 5
tmin = -10
tmax = 10

#A time vector from -10 to 10
a_t = np.linspace(-10,10,num=10)

#Finds the two roots of the equation, with initial guesses at the boundaries
#The t value
t_root_1 = my_Newton(ht, dtht,2)
t_root_2 = my_Newton(ht,dtht,9)
print "The value of the first root is %1.3f" % t_root_1
print "The value of the second root is %1.3f" % t_root_2
print "Which means that the values of F(t) & G(t) are %1.3f & %1.3f" % (t_root_1, t_root_2)

#Finds the roots of the F(x) function
ft_1 = ft(t_root_1)
ft_2 = ft(t_root_2)

#Finds the roots of the G(x) function
gt_1 = gt(t_root_1)
gt_2 = gt(t_root_2)


#Plots the graph and crossover point
plt.figure(1)
plt.plot(a_t,ft(a_t), 'r--')
plt.plot(a_t,gt(a_t), 'k--')
plt.plot(t_root_1,gt_1, 'ko')
plt.plot(t_root_2,gt_2,'ro')
plt.xlabel("Time (s)")
plt.ylabel("Value of function")
plt.title("Crossover point of F(x) & G(x)")

plt.savefig("Hw4 Problem 2 graph")




