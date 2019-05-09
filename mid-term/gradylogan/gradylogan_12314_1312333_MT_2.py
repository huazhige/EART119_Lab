# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils
import math


# create the bounds for finding the root -10<x<10
x = np.linspace (-10, 10, 1000)
# Iterates 1000 times within the bounds

#====================================================
# Functions
#====================================================

def f1(x):
    return x**5+((2/5)*x**2)-2


def f2(x):
    return (np.exp(x/10))+x


def f3(x):
    return (10*(np.sin(x/4)))+(.1*(x+12))

#All of these functions are within the bounds of x defined above
    
#====================================================
# Roots
#====================================================
    
#Use opt_utils.my_Secant to find the roots of the functions without having to find the derivatives

root1 = opt_utils.my_Secant( f1, -1, 1, tol = 1e-7, N = 100)
#The bounds for this root must be smaller than the other functions since the root
#gets so close to zero that python cannot complete the task. It simply says
#cannot divide by zero, so by upping the steps and lowering the bounds, there is 
#enough attempts to find the root.
root2 = opt_utils.my_Secant( f2, -10, 10, tol = 1e-4, N = 20)
root3 = opt_utils.my_Secant( f3, -10, 10, tol = 1e-4, N = 20)

#====================================================
# Plotting
#====================================================

plt.figure()
p1 = plt.subplot(311)
p1.plot(x, f1(x), 'r-')
p1.plot([root1], [f1(root1)], 'r*', ms = 15)

p2 = plt.subplot(312)
p2.plot(x, f2(x), 'b-')
p2.set_ylabel('f(x)')
p2.plot([root2], [f2(root2)], 'b*', ms = 15)

p3 = plt.subplot(313)
p3.plot(x, f3(x), 'k-')
p3.plot([root3], [f3(root3)], 'k*', ms = 15)
p3.set_xlabel('x')

plt.savefig('Midterm_Prob2_Plot')
