"""
Lili Callahan
Homework #4

"""

#   Problem 4
"""
This problem computes the roots for three functions using the Secant method.

"""
#   a)

import numpy as np
import opt_utils

#   a)

def f1(x):
    return -(x**5) + (x**2)/3 + 0.5

f1_sec = opt_utils.my_Secant(f1, 1, 10, tol = 1e-4, N = 20)

print "The root for f1 is at x =", str(f1_sec)

#   b)

def f2(x):
    return np.cos(x)**2 + 0.1

#f2_sec = opt_utils.my_Secant(f2, -10, 10, tol = 1e-4, N = 20)

"""
There exists no root for y = (cos(x))^2 + 0.1 b/c fcm never crosses the x-axis.

"""

#   c)

def f3(x):
    return np.sin(x/3) + (0.1)*(x + 5)

f3_sec = opt_utils.my_Secant(f3, -3, 3, tol = 1e-4, N = 20)

print "The root for f3 is at x =", str(f3_sec)





