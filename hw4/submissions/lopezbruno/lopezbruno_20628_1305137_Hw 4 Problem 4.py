# -*- coding: utf-8 -*-
#Python 2.7, Anaconda 2
"""
Created on Sun May  5 12:04:14 2019

@author: Luno Bropez
"""

'''
Finds the root of a functionusing the secant method
for the 2nd function, there was no root and I threw in
the graph of the second one to show that it does not cross
the x-axis
'''

#===============Functions=========================

import numpy as np
import matplotlib.pyplot as plt


#The FUnction -x^5 + 1/3x^2 + 0.5
def fx_1(x):
    return -x**5 + (0.3333 * (x**2)) + 0.5

#The function cos^2(x) + 0.1
def fx_2(x):
    return (np.cos(x)**2) + 0.1
#The function sin(x/3) + 0.1(x + 5)
def fx_3(x):
    return np.sin(x/3) + (0.1 * (x + 5))

#The my_Secant function from class
def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x_next
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        print i, abs( fct( x1)), x_next
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)
#The root of the first function    
fx_a = my_Secant(fx_1, 1, -2)
#The root of the second function
fx_b = my_Secant(fx_2, 1, 3)
#The root of the third function
fx_c = my_Secant(fx_3, -1, 1.5)

print ("The root of the first function is %1.3f") % fx_a
print("The root of the second function is %s, which means that the function dosen't cross the x-axis") % fx_b
print("The root of the third function is %1.3f") % fx_c

#I included a graph of the second function, to show that it
#does not cross the x-axis
s_t = np.linspace(-10,10,100)

plt.figure(1)

plt.plot(s_t, fx_2(s_t), 'r--')
plt.xlabel("Interval from -10 to 10")
plt.ylabel("The value of the function")
plt.title("The second function has no root" )

