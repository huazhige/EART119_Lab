# -*- coding: utf-8 -*-
#python 3.6
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

########################## 3 ##########################

def fct(t):
    return 1.1*((t-2.5)**2)

def dfdt(t):
    return 2*1.1*(t-2.5)

def my_Newton(fct, dfdx, x0):
    '''
    implementation of Newtons method for solving f(x) = 0,
    when f'(x) is known
    '''
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 0
    while abs(fct(xn**(i+1)) - fct(xn**(i))) < eps and i < N:
        x_next = xn - fct(xn)/dfdt(xn)
        print(i, 'fct value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan


x0 = -9
#independent variable range
xmin, xmax = -10, 15

#### Find Roots
x_root   = my_Newton(fct, dfdt, x0)

#### Plots
a_x = np.linspace(xmin, xmax, 1000)
plt.figure()
plt.plot(a_x, fct(a_x), 'k-')
plt.plot([x_root], [fct(x_root)], 'r*', ms = 14)
plt.plot([xmin, xmax], [0,0], 'r--')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Fct values f(x)')
plt.show()
