import numpy as np
import matplotlib.pyplot as plt
import opt_utils as utils


def fct_f1(x):
    return x**5 + 0.4*x**2 - 2

def dfdx1(x):
    return 5*x**4 + 0.8*x

def fct_f2(x):
    return np.exp(-0.1*x) + x

def dfdx2(x):
    return -0.1*np.exp(-0.1*x) + 1

def fct_f3(x):
    return 10*np.sin(0.25*x) + 0.1*(x+12)

def dfdx3(x):
    return 2.5*np.cos(0.25*x) + 0.1

xmin, xmax = -10, 10

def my_Secant_1( fct_f1, xmin, xmax, tol = 1e-5, N = 20):
    """
    
    """
    xmin = float( xmin)
    xmax = float( xmax)
    i = 0
    while abs( fct_f1(xmax)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next= xmax - fct_f1( xmax)/dfdx1(xmax)
        
        xmin    = xmax
        xmax    = x_next
        print( i, abs( fct_f1( xmax)), x_next)
        i += 1
    # check if solution converged
    if abs( fct_f1( xmax)) > tol:
        return np.nan
    else:
        return xmax

def my_Secant_2( fct_f2, xmin, xmax, tol = 1e-5, N = 20):
    """
    
    """
    xmin = float( xmin)
    xmax = float( xmax)
    i = 0
    while abs( fct_f2(xmax)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next= xmax - fct_f2( xmax)/dfdx2(xmax)
        
        xmin    = xmax
        xmax    = x_next
        print( i, abs( fct_f2( xmax)), x_next)
        i += 1
        xmin < x_next < xmax
    # check if solution converged
    if abs( fct_f2( xmax)) > tol:
        return np.nan
    else:
        return xmax

def my_Secant_3( fct_f3, xmin, xmax, tol = 1e-5, N = 20):
    """
    
    """
    xmin = float( xmin)
    xmax = float( xmax)
    i = 0
    while abs( fct_f3(xmax)) > tol and i < N:
        # numerical approximation of derivative
        # dfdt  = ( fct_fx_1( xmax) - fct_fx_1(xmin))/(xmax - xmin)
        # basically Newton
        x_next= xmax - fct_f3( xmax)/dfdx3(xmax)
        
        xmin    = xmax
        xmax    = x_next
        print( i, abs( fct_f3( xmax)), x_next, xmin, xmax)
        i += 1
    # check if solution converged
    if abs( fct_f3( xmax)) > tol:
        return np.nan
    else:
        return xmax


x_root_1 = my_Secant_1( fct_f1, xmin, xmax, tol = 1e-5, N = 20)
x_root_2 = my_Secant_2( fct_f2, xmin, xmax, tol = 1e-5, N = 20)
x_root_3 = my_Secant_3( fct_f3, xmin, xmax, tol = 1e-5, N = 20)


a_x_1 = np.linspace( xmin, xmax, 1000)

plt.figure(1)
plt.plot( a_x_1, fct_f1(a_x_1), 'k-')
plt.plot( [x_root_1], [fct_f1(x_root_1)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()

a_x_2 = np.linspace( xmin, xmax, 1000)

plt.figure(2)
plt.plot( a_x_2, fct_f2(a_x_2), 'k-')
plt.plot( [x_root_2], [fct_f2(x_root_2)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()

a_x_3 = np.linspace( xmin, xmax, 1000)

plt.figure(3)
plt.plot( a_x_3, fct_f3(a_x_3), 'k-')
plt.plot( [x_root_3], [fct_f3(x_root_3)], 'b*', ms = 10)
plt.grid( True)
plt.xlabel( 'x')
plt.ylabel( 'Fct values f(x)')
plt.show()