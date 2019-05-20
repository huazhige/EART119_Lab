# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#=================================
#function
#=================================

def f1(x):
    return -x**5 + (1/3)*x**2 + .5
def f2(x):
    return (np.cos(x))**2 + .1
def f3(x):
    return np.sin(x/3) + .1*(x+5)

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    """
    
    """
    x0 = float( x0)
    x1 = float( x1)
    i = 0 
    while abs( fct(x1)) > tol and i < N:
        #numerical approx of derivative
        dfdt = (fct( x1) - fct( x0))/( x1 - x0)
        #basically Newton
        x_next = x1 - fct( x1)/dfdt
        
        x0 = x1
        x1 = x_next
        print( i, 'fct_value', abs(fct( x1)), x_next)
        
        i += 1
    #check if solution converged
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1
    
#====================================
#parameters
#====================================

xmin, xmax = -10, 10
x3min, x3max = -3, 3

x0 = 3
x1 = -1

x_root = my_Secant( f1, x0, x0+10)
x2_root = my_Secant( f2, x0, x0+10)
x3_root = my_Secant( f3, x1, x1+10)

#=====================================
#plot
#=====================================

a_x = np.linspace( xmin, xmax, 1000)
plt.figure(1)
plt.plot( a_x, f1(a_x), 'k-')
plt.plot( [x_root], [f1(x_root)], 'r*', ms = 14)
plt.plot( [xmin,xmax], [0,0], 'r--')
plt.grid(True)
plt.xlabel( 'x')
plt.ylabel( 'Fct Values f(x)')
plt.show()

plt.figure(2)
plt.plot( a_x, f2(a_x), 'k-')
plt.plot( [x2_root], [f2(x2_root)], 'r*', ms = 14)
plt.plot( [xmin,xmax], [0,0], 'r--')
plt.grid(True)
plt.xlabel( 'x')
plt.ylabel( 'Fct Values f(x)')
plt.show()

a_x3 = np.linspace( x3min, x3max, 1000)
plt.figure(3)
plt.plot( a_x3, f3(a_x3), 'k-')
plt.plot( [x3_root], [f3(x3_root)], 'r*', ms = 14)
plt.plot( [x3min,x3max], [0,0], 'r--')
plt.grid(True)
plt.xlabel( 'x')
plt.ylabel( 'Fct Values f(x)')
plt.show()



