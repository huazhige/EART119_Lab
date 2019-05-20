# -*- coding: utf-8 -*-
#python 3.6
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

##### Func definitions
def f1(x):
    return -x**5 + (1/3)*x**2 + .5
def dfdx(x):
    return -5*x**4 + (2/3)*x

def f2(x):
    return (np.cos(x))**2 + .1
def dfdx2(x):
    return -2*np.sin(x)*np.cos(x)

def f3(x):
    return np.sin(x/3) + .1*(x+5)
def dfdx3(x):
    return (1/3)*np.cos(x/3) + .1

def my_Secant(f1, x0, x1, tol = 1e-5, N = 20):
    '''
    '''
    x0 = float(x0)
    x1 = float(x1)
    i  = 0
    while abs(f1(x1)) > tol and i < N:
        #numerical approximation of derivative
        dfdt = (f1(x1) - f1(x0))/(x1-x0)
        #basically Newton
        x_next = x1 - f1(x1)/dfdt
        x0     = x1
        x1     = x_next
        i     += 1
        #check if solution converged
        if abs(f1(x1)) > tol:
            return np.nan
        else:
            return x1
        
def my_Secant2(f2, x0, x1, tol = 1e-5, N = 20):
    '''
    '''
    x0 = float(x0)
    x1 = float(x1)
    i  = 0
    while abs(f2(x1)) > tol and i < N:
        #numerical approximation of derivative
        dfdt = (f2(x1) - f2(x0))/(x1-x0)
        #basically Newton
        x_next = x1 - f2(x1)/dfdt
        x0     = x1
        x1     = x_next
        i     += 1
        #check if solution converged
        if abs(f2(x1)) > tol:
            return np.nan
        else:
            return x1
        
def my_Secant3(f3, x0, x1, tol = 1e-5, N = 20):
    '''
    '''
    x0 = float(x0)
    x1 = float(x1)
    i  = 0
    while abs(f3(x1)) > tol and i < N:
        #numerical approximation of derivative
        dfdt = (f3(x1) - f3(x0))/(x1-x0)
        #basically Newton
        x_next = x1 - f3(x1)/dfdt
        x0     = x1
        x1     = x_next
        i     += 1
        #check if solution converged
        if abs(f3(x1)) > tol:
            return np.nan
        else:
            return x1
        
x0 = -9
xmaxf12, xminf12 = -10, 10
xmaxf3, xminf3 = -3, 3
x_rootSc = my_Secant(f1, x0 , x0+10)
print(x_rootSc)
x_rootSc2 = my_Secant2(f2, x0 , x0+10)
print(x_rootSc2)
x_rootSc3 = my_Secant3(f3, x0 , x0+10)
print(x_rootSc3)


a_x = np.linspace(xminf12, xmaxf12, 1000)
a_x1 = np.linspace(xminf3, xmaxf3, 1000)
plt.figure(1)
plt.plot(a_x, f1(a_x), 'r-')
plt.plot([x_rootSc], [f1(x_rootSc)], 'b*', ms = 12)
plt.show()
plt.figure(2)
plt.plot(a_x, f2(a_x), 'r-')
plt.plot([x_rootSc2], [f2(x_rootSc2)], 'b*', ms = 12)
plt.show()
plt.figure(3)
plt.plot(a_x1, f3(a_x1), 'r-')
plt.plot([x_rootSc3], [f3(x_rootSc3)], 'b*', ms = 12)
plt.show()
