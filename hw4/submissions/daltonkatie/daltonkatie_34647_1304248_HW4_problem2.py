# -*- coding: utf-8 -*-
"""

        Find the intersection (cross-over point) between 
        the two functions using Newton’s method

"""
import numpy as np
import opt_utils
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
#       parameters and functions
#------------------------------------------------------------------------------
time = np.linspace(-10,10,1000)

#f(t) 
def f_t(x):
    return (1.1*(x-2.5)**2)

#derivative of f(t)
def df_t(x):
    return (2.2*(x-2.5))

#g(t)
def g_t(x):
    return (5 * x + 2.5)

#derivative of g(t)
def dg_t(x):
    return (5)

#f(t) - g(t)
def fg_t(x):
    return((1.1*(x-2.5)**2)-(5 * x + 2.5))
    
#f'(t) - g'(t)
def dfg_t(x):
    return(2.2*(x-2.5) - 5)

#------------------------------------------------------------------------------
#       use newtons' method thru opt_utils
#------------------------------------------------------------------------------
root1 = opt_utils.my_Newton(fg_t, dfg_t, 50)
print('There is a cross-over at time: ',root1)

root2 = opt_utils.my_Newton(fg_t, dfg_t, 1)
print('There is a cross-over at time: ',root2)

#------------------------------------------------------------------------------
#       plot
#------------------------------------------------------------------------------
plt.plot(time, fg_t(time), 'ro' , ms = 2)
plt.plot([root1, 0],[root2,0], 'ko', ms = 3)
plt.xlabel('Time')
plt.ylabel('Function')
plt.grid(True)
plt.show()