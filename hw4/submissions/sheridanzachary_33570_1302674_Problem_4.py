# -*- coding: utf-8 -*-

import numpy as np
#======================function definitions===================================
def fct1(x):
    return -x**5.+(1./3.)*x**2.+0.5

def fct2(x):
    return (np.cos(x))**2.+0.1

def fct3(x):
    return np.sin(x/3.)+0.1*(x+5.)

def my_secant(fct, x0, x1, tol=1e-6, N=20):
    x0 = float(x0)
    x1 = float(x1)
    i  = 0
    while abs(fct(x0)) > tol and i < N:
        dfdx = (fct(x1)-fct(x0))/(x1-x0)
        x2   = x1-(fct(x1)/dfdx)
        x0   = x1
        x1   = x2
        i += 1
    if abs(fct(x0)) > tol:
        return np.nan
    else:
        return x1
#====================parameters===============================================
xmin_f1, xmax_f1 = -10, 10
xmin_f2, xmax_f2 = -10, 10
xmin_f3, xmax_f3 = -3, 3
a_x = np.linspace(xmin_f1, xmax_f1, 1000)
a_x3 = np.linspace(xmin_f3, xmax_f3, 1000)

root_f1 = my_secant(fct1, 0.6, 2)
root_f2 = my_secant(fct2, -5, 5)
root_f3 = my_secant(fct3, -3, 3)
#==================roots===================================================
print 'root of function 1:', root_f1 #0.9577
print 'root of function 2:', root_f2 #DNE
print 'root of function 3:', root_f3 #-1.1768




