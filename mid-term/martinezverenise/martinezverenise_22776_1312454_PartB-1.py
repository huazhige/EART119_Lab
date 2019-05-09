# -*- coding: utf-8 -*-
""" 
- we will be finding the roots for each of the three given functions
   - f1 = x**5 +(2/5)*x**2 - 2
   - f2 = exp((-1/10)*x) +x
   - f3 = 10*sin((1/4)*x)+ .1*(x+12)
- all within the interval [-10,10]
"""
import matplotlib.pyplot as plt
import numpy as np 
def f1(x):
    return  x**5 +(2/5)*x**2 - 2
def dfdt1(x):
    return 5*x**4 +(1/5)*x 
def f2(x):
    return np.exp((-1/10)*x) +x
def dfdt2(x):
    return (-1/10)*np.exp((-1/10)*x) +1
def f3(x):
    return 10*np.sin((1/4)*x)+ .1*(x+12)
def dfdt3(x):
    return (10/4)*np.cos((1/4)*x) + .1
"""
Here we are using the secant method to find the roots of each individual function 
"""
def secant1(f1, x0, x1, tol=1e-5, N = 20):  
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(f1(x1)) > tol and i < N:
        dfdt = (f1(x1) - f1(x0))/(x1-x0)
        #bassically newton
        x_next = x1 - f1(x1)/dfdt
        x0 = x1
        x1 = x_next 
        i += 1 
    #check i solution converges 
    if abs(f1(x1)) > tol:
        return np.nan
    else:
        return x1


def secant2(f2, x0, x1, tol=1e-5, N = 20):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(f2(x1)) > tol and i < N:
        dfdt = (f2(x1) - f2(x0))/(x1-x0)
        #bassically newton
        x_next = x1 - f2(x1)/dfdt
        x0 = x1
        x1 = x_next 
        
        i += 1 
    #check i solution converges 
    if abs(f2(x1)) > tol:
        return np.nan
    else:
        return x1
    
def secant3(f3, x0, x1, tol=1e-5, N = 20):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(f3(x1)) > tol and i < N:
        dfdt = (f3(x1) - f3(x0))/(x1-x0)
        #bassically newton
        x_next = x1 - f3(x1)/dfdt 
        x0 = x1
        x1 = x_next 
        
        i += 1 
    #check i solution converges 
    if abs(f3(x1)) > tol:
        return np.nan
    else:
        return x1
    
    
################################## Parameters##################################
x0 = -9
xmax, xmin= -10, 10 
###############################################################################
x_roots_f1 = secant1(f1, x0, x0+10)
x_roots_f2 = secant2(f2, x0, x0+10)
x_roots_f3 = secant3(f3, x0, x0+10)
x = np.linspace(xmax, xmin, 1000)
###############################   Plots    ###################################
plt.figure(1)
plt.plot(x, f1(x), 'k-')
plt.plot(x_roots_f1, f1(x_roots_f1), 'b*', ms=12)
plt.figure(2)
plt.plot(x, f2(x), 'k-')
plt.plot(x_roots_f2, f2(x_roots_f2), 'b*', ms=12)
plt.figure(3)
plt.plot(x, f3(x), 'k-')
plt.plot(x_roots_f3, f3(x_roots_f3),'b*', ms =12) 