# -*- coding: utf-8 -*-
"""
        Modify the function we developed in class for Newton’s method
        so that the iteration (while loop) stops if  the following
        convergence criterion is met
"""
#------------------------------------------------------------------------------
#       ORIGIONAL FUNCTION
#------------------------------------------------------------------------------
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
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)

#Create a function to test what the root should be
import numpy as np
import matplotlib.pyplot as plt

time1 = np.linspace(-5,5, 100)
def f1_x(x):
    return((x+2)**2 - 3)
    
def df1_x(x):
    return (2*(x+2))
plt.figure(1)
plt.plot(time1, f1_x(time1), 'ro', ms = 2)
 #play with this range until the plot is precise
plt.show()

root = my_Newton(f1_x, df1_x, 2)
print(root)


#------------------------------------------------------------------------------
#       NEW FUNCTION
#------------------------------------------------------------------------------
def my_Newton_new( fct, df_dt, x0, tol = 1e-4, N = 20):
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
    while abs( fct( xn)) > tol and i < N: 
        if (fct(xn**(i+1))-fct(xn**(i))) < tol: #add in this clause to stop the loop if this is true
            return ('Convergence Criteria Met at:', xn )
        else:
            x_next = xn - fct( xn)/df_dt( xn)
            print i, abs( fct( xn)), x_next
            xn = float( x_next)
            i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)
    
    

root_new = my_Newton_new(f1_x, df1_x, 2)
print(root_new)