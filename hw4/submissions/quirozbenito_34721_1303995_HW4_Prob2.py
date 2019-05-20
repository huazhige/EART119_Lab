# -*- coding: utf-8 -*-
"""
Benny Quiroz
Earth 119
Homework 4 Problem 2
"""
import numpy as np
import matplotlib.pyplot as plt
import modules.opt_utils as ou

"""
For part a, let's just graph the functions
"""
def f_(t):
    return 1.1*(t - 2.5)**2
def g_(t):
    return 5*t + 2.5
def fgdiff(t):
    return f_(t) - g_(t)
def compderiv(t):
    return 2.2*(t - 2.5) - 5

a_t = np.linspace(-10,10,1000)
plt.cla()
plt.figure(1)
plt.plot(a_t, f_(a_t), 'r-')
plt.plot(a_t, g_(a_t), 'b-')

"""
By looking at it, the two funcitons intersect twice.
"""
"""
For part b we will employ Newton's method.
"""

#Chose my guesses by looking at the figure. 
#Stores the times of intersection, and function values at that time. 
intersect1 = ou.my_Newton(fgdiff, compderiv, -1)
f_1 = f_(intersect1)
g_1 = g_(intersect1)
intersect2 = ou.my_Newton(fgdiff, compderiv, 10)
f_2 = f_(intersect2)
g_2 = g_(intersect2)

"""
Now lets use a more rudimentary method for finding the intersections.
"""
#Arrays of y-values
a_ft  = f_(  a_t)
a_gt  = g_(  a_t)

#Difference of y-values
a_df_g  = a_ft - a_gt
## Bool array that will find all cross-over points with discretion of 0.1
sel = abs(a_df_g) < 0.1

#Applying the bool array to all of our arrays to find the intersection points. 
a_T = a_t[sel]
fbad = f_(a_T)
gbad = g_(a_T)

plt.figure(2)
plt.plot(a_t, fgdiff(a_t), 'k-', label = 'f(x) - g(x)')
plt.plot(a_T, fgdiff(a_T), 'bo', ms = 5, label = 'Rudimentary method')
plt.plot(intersect1, f_1 - g_1, 'go', ms = 5, label = 'Newtons')
plt.plot(a_t,a_t*0, 'r-', lw = 1, label = 'y = 0: for comparison')
#Choosing this window allows us to zoom in on the first point and get clarity 
#on how good each appoximation is. 
plt.xlim(0.4, 0.5)
plt.ylim(-0.5, 0.5)
plt.legend()
plt.show()
