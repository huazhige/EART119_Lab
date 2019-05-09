# -*- coding: utf-8 -*-

"""

Question 2 Roots

"""


import numpy as np
import matplotlib.pyplot as plt
import os

#========================================================
#                   Functions
#========================================================
def f1 (x):
    return x**5 + (2/5)*(x**2) - 2
def f2 (x):
    return np.exp(-x/10) +x
def f3 (x):
    return 10*np.sin(x/4) + 0.1*(x+12)


def df2(x):
    return (-1/10)*np.exp(-x/10) +1

#========================================================
#                   Root Finding
#========================================================
def my_Secant( fct, x0, x1, tol = 1e-6, N = 20):
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


print my_Secant(f1, 0, 1.1)
print my_Secant(f2, -2, -1)
print my_Secant(f3, -1, 1)




"""
f1 1
f2 -1
f3 -.1
"""

#========================================================
#                   Plots
#========================================================


x = np.arange(-10, 11)

plt.figure(1)
plt.title('Question 2')
plt.plot(x, f1(x), label = 'f1, root: 1.1486983547')
plt.plot(x, f2(x), label = 'f2 root: -1.11832609375')
plt.plot(x, f3(x), label = 'f3 root: -0.462528886891')
plt.plot(1.14869713548, 0, 'ro')
plt.plot(-0.462525085242, 0, 'ro')
plt.plot(-1.11832609375, 0, 'ro')
#plt.plot(x, 0)

plt.ylim(-10, 10)
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')



plt.savefig( 'Q2plt')
plt.show()
