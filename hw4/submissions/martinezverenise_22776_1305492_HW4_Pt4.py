"""
python3.7
- We will us the secant method to find the roots for f1, f2, f3
"""
import matplotlib.pyplot as plt
import numpy as np 
def f1(x):
    return -x**5 + (1/3)*x**2 +.5
def dfdt1(x):
    return -5*x**4 + (2/3)*x
def f2(x):
    return np.cos(x)**2 + .1
def dfdt2(x):
    return -2*np.sin(x)*np.cos(x)
def f3(x):
    return np.sin(x/3) + .1*(x+5)
def dfdt3(x):
    return (1/3)*np.cos(x/3) +.1

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
xmaxf12, xminf12 = -10, 10
xmaxf3, xminf3 = -3, 3 
###############################################################################
x_roots_f1 = secant1(f1, x0, x0+10)
x_roots_f2 = secant2(f2, x0, x0+10)
x_roots_f3 = secant3(f3, x0, x0+10)
x = np.linspace(xmaxf12, xminf12, 1000)
x_3 = np.linspace(xmaxf3, xminf3, 1000)
 
plt.figure(1)
plt.plot(x, f1(x), 'k-')
plt.plot(x_roots_f1, f1(x_roots_f1), 'b*', ms=12)
plt.figure(2)
plt.plot(x, f2(x), 'k-')
plt.plot(x_roots_f2, f2(x_roots_f2), 'b*', ms=4)
plt.figure(3)
plt.plot(x_3, f3(x_3), 'k-')
plt.plot(x_roots_f3, f3(x_roots_f3),'b*', ms =12) 


