# -*- coding: utf-8 -*-

# my_Newton from opt_utils

def my_Newton( fct, df_dt, x0, x1, tol = 1e-6, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    xn1= float(x1)
    i  = 0
    
    while abs(f(xn1)-f(xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        #print 'f(n) ' + str(f(xn)) + ' and f(n1) ' + str(f(xn1))
              
        x_next = xn1 - fct( xn1)/df_dt( xn1)
        print i, abs( fct( xn1)), x_next
        xn = xn1
        xn1 = float( x_next)

        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)
    
# just tesing the function
import numpy as np
import matplotlib.pyplot as plt
    
def f(t):
    return np.sin(t)

def dfdt(t):
    return np.cos(t)   

x0 = 6
x1 = x0+0.1
xx = np.linspace(0,4*np.pi)

test = my_Newton( f, dfdt, x0, x1, 0.00001)
print ('test ' + str(test))

plt.plot(xx, f(xx), 'b')
plt.plot(test, f(test), 'r o')