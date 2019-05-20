# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:47:38 2019

@author: Brady

Homework problem 2: finding cross over opoints using Newton or Secant method
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt
import os

N = 1000
tmin= -10
tmax= 10
t = np.linspace(tmin, tmax, N-1) 
c= 1.1
A= 5
t0= 2.5
x0= -10



def f(t):
    return c*(t-t0)**2
def dfdx(t):
    return 2.2*t-10.5
def g(t): 
    return A*t+t0
def dg_dx(t):
    return 5.0
def h(t):
    # f(t) - g(t)
    return (1.1*(t)**2)-(10.5*t)+(4.375)
def dh_dt(t):
    return 2.2*(t)-10.5

point_of_int = opt.my_Newton( h, dh_dt, x0, tol = 1e-5, N=50)

print('the functions intersect at the value t = %.3f') % (point_of_int)
print('the functions intesect 2 times in the interval t=[-10,10].')


a_t = np.linspace(tmin, tmax, N)
a_ft = f(a_t)
a_gt = g(a_t)
a_ht = h(a_t)

plt.plot(a_t, a_ht, 'ro', ms=2)
plt.plot(a_t, a_ft, 'go', ms=2)
plt.plot(a_t, a_gt, 'bo', ms=2)

dir_out = './'
file_out='Homeworkq2crossoverpts.png' 
os.chdir( dir_out)
plt.savefig( file_out)

plt.show
#There are two cross over points in the intwerval -10=<t=<10
#t=.437, 9.109, f(t) = g(t) at 4.683, 48.044
    
    
    
    
    
    
    
    
