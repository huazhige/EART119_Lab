"""
Lili Callahan
Homework #4

"""

#   Problem 2
"""
This problem computes the intersection points between two functions.

"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

#   parameters and variables
t0 = 2.5
c = 1.1
A = 5
t = np.arange(-10, 11)

def f(t):
    return c*((t - t0)**2)

def g(t):
    return A*t + t0

#   a)

#   create function for f(t) - g(t)
def F(t):
    return c*((t - t0)**2) - (A*t + t0)

#   compute derivative of F(t)
def dFdt(t):
    return c*t*2 - c*t0*2 - A

plt.figure()
plt.plot(t, f(t))
plt.plot(t, g(t))
plt.xlim(-10, 10)
plt.show()

"""
From this graph, you can see that the two functions intersect twice on the interval from (-10, 10).

"""

#   b) 

#   find first intersection point
newton = opt_utils.my_Newton(F, dFdt, -10, tol = 1e-4, N = 20)

print "The crossover point is at x =", str(newton), "y =", str(f(newton))

#   find second intersection point
newton2 = opt_utils.my_Newton(F, dFdt, 10, tol = 1e-4, N = 20)

print "The crossover point is at x =", str(newton2), "y =", str(f(newton2))

#   c)

""" 
The cross value is taken from the week 2 in-class assignment

"""

cross = 0.43521761

plt.figure()
plt.plot(t, F(t))
plt.plot(newton, f(newton), marker = 'o')
plt.plot(cross, f(cross), marker = 'o')
plt.savefig('2_graph')
plt.show()




    