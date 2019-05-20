# -*- coding: utf-8 -*-
#python2.7


# =============================================================================
#                              Problem 2.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import os
import opt_utils as opt

# =============================================================================
#                          Define functions
# =============================================================================

def f ( t):
    """
    The function f given in homework 4 problem 2
    """
    
    c = 1.1
    t_0 = 2.5

    Ans = c * (t - t_0)**2
    
    return Ans

def g ( t):
    """
    The function g given in homework 4 problem 2
    """
    
    t_0 = 2.5
    A = 5.
    
    Ans = A * t + t_0
    
    return Ans

def diff ( t):
    """
    f(t) minus g(t)
    """
    
    c = 1.1
    t_0 = 2.5
    A = 5.
    
    Ans = (c * (t - t_0)**2) - (A * t + t_0)
    
    return Ans

def dfdt ( t):
    """
    The derivative of f(t)
    """
    c = 1.1
    t_0 = 2.5
    
    Ans = 2*c*(t-t_0)
    
    return Ans

def dgdt ( t):
    """
    The deriviative of g(t)
    """
    A = 5.
    
    Ans = A
    
    return Ans

def ddiffdt ( t):
    """
    Derivative of the diff function
    
    The name is d(diff)/dt
    """
    
    c = 1.1
    t_0 = 2.5
    A = 5.
    
    Ans = 2*c*(t-t_0) - A
    
    return Ans

# =============================================================================
#                           Define variables
# =============================================================================

t0 = 2.6 # Guess for where the root is
t = np.arange(-10, 11, 1)
# print(t) # Unit testing

t_root = opt.my_Newton(diff, ddiffdt, t0)

for i in np.arange(0,21,1):
    if t_root == t[i]:
        print t_root
    if i < 20:
        i += 1
    else:
        break
    
# For some reason, even though I'm setting it to a variable, the my_Newton 
# function is still printing variables. I'm assuming this is causing 
# the for loop I created to not work, as the code "print t_root" simply isn't
# doing anything

# From here I would see how many numbers are printed, allowing me to solve 
# part a. I can see which values of t are the roots from what's printed. From
# here I can plug these values into f(t) and g(t) to solve part b.
# The following is what I would type for part c.

# =============================================================================
# plt.plot(t, diff(t), 'b-')
# plt.plot('one of the printed roots', diff('that root'), 'r*')
# plt.savefig('HW4_Problem2_plot.png')
# =============================================================================
