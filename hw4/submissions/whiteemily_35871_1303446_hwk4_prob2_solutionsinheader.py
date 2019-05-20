# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:51:51 2019

@author: Emily White
"""
"""
        Find the intersection (cross-over point)between the 
        following two functions using Newton’s or the Secant method
        (Hint: solve for f(t) - g(t) = 0)
        
a) How many cross-over points are there for −10≤t≤10?
    ANS: there are 4 points
    
b) What are the values of t, f(t) and g(t)?
    ANS: (0, 'fct_value', 5.025, 0.7396373056994818)
(1, 'fct_value', 2.789422031463931, 0.4147721272647731)
(2, 'fct_value', 0.20913217303120302, 0.4374296335410884)
(3, 'fct_value', 0.0075319994515474775, 0.4366419798977052)
(4, 'fct_value', 1.8948456016687487e-05, 0.43663999337845666)

c) see .png file

"""
import numpy as np
import matplotlib.pyplot as plt

#=============================================================================
#                  variable dfns
#=============================================================================
c   =   1.1 
t_ini  =   2.5 #t initial value
A   =   5
 
#=============================================================================
#                   fnc defns
#=============================================================================
def fct(t):
# f(t) - g(t) == c*(t-t_ini)**2 - A*t - t_ini
# f(t) = c*(t-t_ini)**2
# g(t) = A*t + t_ini
    return c*(t - t_ini)**2 - A*t - t_ini

def dfdt(t):
# dervivative of f(t) - g(t)
    return 2*c*(t - t_ini) - A


def my_Newton( fct, df_dt, t0):
    """
- implementation of Newton's method for solving f(t) - g(t) = 0, when fct'(t) is known
    """
    tn = float(t0)
    eps = 1e-5 #value close enough to zero
    N = 20
    i = 0
    while fct(tn) < eps and i < N:
        t_next = tn - fct(tn)/df_dt(tn)
        print(i, 'fct_value', abs(fct(tn)), t_next) #gets it close to 0, ie the purpose
        tn = t_next
        i += 1
    if abs(fct(tn)) < eps:
        return t_next
    else: #soln did not converge
        return np.nan
#returning nan as a soln to say it did not converge
     
def my_Secant(fct, t0, t1, tol = 1e-5, N = 20):
    
  #  tol = tolerance
    
    t0 = float(t0)
    t1 = float(t1)
    i = 0
    while abs(fct(t1)) > tol and i < N:
        #numerical approx of derivative
        dfdg = (fct(t1) - fct(t0))/(t1-t0)
        t_next = t1 - fct(t1)/dfdg
        
        t0 = t1
        t1 = t_next
        print(i, 'fct_value', abs(fct(t0)), t_next)
        i+= 1
    # check if soln converged
    if abs(fct(t1)) > tol:
        return np.nan
    else:
        return t1

#=============================================================================
#                       parameters
#=============================================================================
t0 = -9
#independent variable range
xmin, xmax = -10, 10

#=============================================================================
#                   find roots
#=============================================================================
t_root = my_Newton(fct, dfdt, t0)
#
t_rootSec = my_Secant(fct, t0, t0+10)
#=============================================================================
#                   plots!!
#=============================================================================
a_t = np.linspace(xmin, xmax, 1000)

plt.figure(2)
plt.plot(a_t, fct(a_t), 'k-')
plt.plot([t_root], [fct(t_root)], 'r*', ms = 14)
plt.plot([t_rootSec], [fct(t_rootSec)], 'b*', ms = 10) #b* blue star, ms is size of star
plt.plot([xmin, xmax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Fct values f(x)')
plt.show()
