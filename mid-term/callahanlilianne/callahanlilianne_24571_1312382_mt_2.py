"""
Lili Callahan
Midterm Problem 2

"""

import numpy as np
import matplotlib.pyplot as plt

#############################################################################
#       Finding Roots
##############################################################################

x = np.arange(-10, 11)

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

# a)

def f1(x):
    return x**5 + ((2*x**2)/5) - 2.

f1_sec = my_Secant(f1, -10, 10, tol = 1e-4, N = 20)

print "The root for f1 is at x =", str(f1_sec)

# b)
    
def f2(x):
    return np.exp(-x/10) + x

f2_sec = my_Secant(f2, -10, 10, tol = 1e-4, N = 20)

print "The root for f2 is at x =", str(f2_sec)

# c)

def f3(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)

f3_sec = my_Secant(f3, -10, 10, tol = 1e-4, N = 20)

print "The root for f3 is at x =", str(f3_sec)

#############################################################################
#       Plotting
##############################################################################

plt.figure()
plt.subplot(311)
plt.plot(x, f1(x), label = "Root is at x = 1.09")
plt.legend( loc = 'upper right')
plt.ylabel("f1(x)")
plt.ylim(-200, 200)
plt.subplot(312)
plt.plot(x, f2(x), label = "Root is at x = -1.12")
plt.legend( loc = 'upper right')
plt.ylabel("f2(x)")
plt.subplot(313)
plt.plot(x, f3(x), label = "Root is at x = -0.46")
plt.legend( loc = 'upper right')
plt.ylabel("f3(x)")
plt.xlabel("x")
plt.savefig("mt_2_plot")
plt.show()







