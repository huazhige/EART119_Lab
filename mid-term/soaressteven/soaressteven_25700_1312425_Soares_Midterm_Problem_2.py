# -*- coding: utf-8 -*-
#python 2.7


import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                     Functions from opt_utils.py
# =============================================================================

# Just to be sure of what code I am using, I will just copy and paste the
# functions from opt_utils.py into here, instead of importing it

# If I am supposed to import it, just know that I know how to do that:
# import opt_utils.py as opt
# Later on I would type opt.my_Newton( fct, df_dt, x0)

def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        #print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)


# =============================================================================
#                             Define functions
# =============================================================================

def f1 ( x):
    return x**5 + (2./5.)*(x**2) - 2.

def f2 ( x):
    return np.exp((-1 * x) / 10.) + x

def f3 ( x):
    return 10 * np.sin(x/4.) + 0.1*(x + 12.)

def df1dx ( x):
    return 5*(x**4) + (4./5.)*x

def df2dx ( x):
    return ((-1.*x)/10.) * np.exp((-1 * x)/10.) + 1

def df3dx ( x):
    return (5./2.) * np.cos(x/4.) + 0.1

# =============================================================================
#                             Define variables
# =============================================================================

N = 1000
x = np.linspace(-10,10,N)

x_root1 = my_Newton(f1, df1dx, 0.01)
x_root2 = my_Newton(f2, df2dx, 0.)
x_root3 = my_Newton(f3, df3dx, 0.1)


# =============================================================================
#                                   Plots
# =============================================================================

plt.subplot(611)
plt.plot(x, f1(x), 'k-')
plt.xlabel('x')
plt.title('f1(x)')
plt.grid()
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_1.png')
plt.subplot(612)
plt.plot(x, f2(x), 'b-')
plt.xlabel('x')
plt.title('f2(x)')
plt.grid()
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_2.png')
plt.subplot(613)
plt.plot(x, f3(x), 'r-')
plt.xlabel('x')
plt.title('f3(x)')
plt.grid()
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_3.png')
plt.subplot(614)
plt.plot([x_root1], f1([x_root1]), 'k*')
plt.xlabel('x')
plt.title('df1/dx')
plt.grid()
plt.legend(str(x_root1))
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_4.png')
plt.subplot(615)
plt.plot([x_root2], f2([x_root2]), 'b*')
plt.xlabel('x')
plt.title('df2/dx')
plt.grid()
plt.legend(str(x_root2))
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_5.png')
plt.subplot(616)
plt.plot([x_root3], f3([x_root3]), 'r*')
plt.xlabel('x')
plt.title('df3/dx')
plt.grid()
plt.legend(str(x_root3))
plt.show()
plt.savefig('Soares_Midterm_Problem_2_Subplot_6.png')