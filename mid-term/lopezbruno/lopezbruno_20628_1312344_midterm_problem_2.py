# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:42:09 2019

@author: bruno
"""

import matplotlib.pyplot as plt
import numpy as np

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


#Creates all of the functions and their derivatives
def fx(x):
    return x**5 + 0.4*(x**2) - 2

def dt_fx(x):
    return 5 * (x**4) + 0.8*x

def fx_1(x):
    return np.exp(-x/10) + x

def dt_fx1(x):
    return -0.1 * np.exp(-x/10) + 1

def fx_3(x):
    return 10 * np.sin(x/4) + 0.1 * x + 1.2

def dt_fx3(x):
    return 2.5 * np.cos(0.25 * x) + 0.1

t_root_1 = my_Secant(fx, 2, 1)
t_root_2 = my_Secant(fx_1,2,1 )
t_root_3 = my_Secant(fx_3, 2, 1)
#Prints out all of the roots
print"This is the root for the first function %1.2f " %t_root_1
print"This is the root for the second function %1.2f " %t_root_2
print"This is the root for the third function %1.2f " %t_root_3

a_t = np.linspace(-10,10,100)

plt.figure(1)
#Plots all of the same graphs together
plt.plot(a_t, fx(a_t), 'r--')
plt.plot(a_t, fx_1(a_t), 'ko')
plt.plot(a_t, fx_3(a_t), 'r--')
plt.ylim(-10,10)

plt.show()
plt.savefig("Midterm Problem 2 Graph")
