# -*- coding: utf-8 -*-
#python 3.6
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils


########################## 2 ##########################
##### Func definitions
dir_out = 'data_2'
def fct(t):
    return 1.1*((t-2.5)**2)

def dfdt(t):
    return 2*1.1*(t-2.5)

def gct(t):
    return 5*t+2.5

def dgdt(t):
    return 5

def my_Newton(fct, dfdt, x0):
    '''
   #implementation of Newtons method for solving f(x) = 0,
   #when f'(x) is known
    '''
    xn = float(x0)
    eps = 1e-6
    N = 25
    i = 0
    while abs(fct(xn)) > eps and i < N:
        x_next = xn - fct(xn)/dfdt(xn)
        print(i, 'fct value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan

def my_Newton1(gct, dfdt, x0):
    '''
   #implementation of Newtons method for solving f(x) = 0,
   #when f'(x) is known
    '''
    xn = float(x0)
    eps = 1e-6
    N = 25
    i = 0
    while abs(gct(xn)) > eps and i < N:
        x_next = xn - gct(xn)/dgdt(xn)
        print(i, 'gct value', abs(gct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(gct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan
x0 = 0

f_t = my_Newton(fct, dfdt, x0)

g_t = my_Newton1(gct, dgdt, x0 )

xmin, xmax = -10, 10
a_x = np.linspace(xmin, xmax, 21)
plt.figure()
plt.plot(a_x, fct(a_x), 'r-')
plt.plot(a_x, gct(a_x), 'b-')
plt.plot([f_t], [fct(f_t)], 'r*', ms = 14)
plt.plot([g_t], [gct(g_t)], 'b*', ms = 14)
plt.plot([f_t - g_t], [fct(f_t) - gct(g_t)], 'g*', ms = 14)  #comparison
plt.plot([xmin, xmax], [0,0], 'r--')
plt.grid(True)
plt.savefig( dir_out)
plt.show()

