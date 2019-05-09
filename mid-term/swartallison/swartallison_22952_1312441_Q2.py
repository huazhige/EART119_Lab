# Allison Swart
# Astro/Earth 119 Midterm
# May 8, 2019

# anaconda2/python2.7

import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define functions
def fct_1( x):
    return x**5 + ( 2 / 5)*x**2 - 2

def fct_2( x):
    return np.exp( - x / 10) + x

def fct_3( x):
    return 10*np.sin( x / 4) + 0.1*( x + 12)

# Define rootfinding method
def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    # when we don't know f'
    x0 = float( x0)
    x1 = float( x1)
    i = 0
    while abs( fct( x1)) > tol and i < N:
        #numerical approximation
        dfdt = (fct( x1) - fct( x0)) / (x1 - x0)
        x_next = x1 - fct( x1) / dfdt
        
        x0 = x1
        x1 = x_next
        i += 1
    #check for convergence
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1

# Define parameters
x0 = -9
xmin, xmax = -10, 10
x_root_fct1 = my_Secant( fct_1, x0, x0 + 10)
x_root_fct2 = my_Secant( fct_2, x0, x0 + 10)
x_root_fct3 = my_Secant( fct_3, x0, x0 + 10)

print 'Fct 1 root = ', x_root_fct1
print 'Fct 2 root = ', x_root_fct2
print 'Fct 3 root = ', x_root_fct3


# GRAPHS

a_x = np.linspace( xmin, xmax, 1000)

plt.figure(1)
plt.plot( a_x, fct_1(a_x), 'b-')
plt.plot( [x_root_fct1], [fct_1( x_root_fct1)], 'b*', ms = 8)
plt.plot( [xmin, xmax], [0, 0], 'r--')
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x1)')
plt.show()

plt.figure(2)
plt.plot( a_x, fct_2( a_x), 'k-')
plt.plot( [x_root_fct2], [fct_2( x_root_fct2)], 'k*', ms = 8)
plt.plot( [xmin, xmax], [0, 0], 'r--')
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x2)')
plt.show()

plt.figure(3)
plt.plot( a_x, fct_3( a_x), 'g-')
plt.plot( [x_root_fct3], [fct_3( x_root_fct3)], 'g*', ms = 8)
plt.plot( [xmin, xmax], [0, 0], 'r--')
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x3)')
plt.show()