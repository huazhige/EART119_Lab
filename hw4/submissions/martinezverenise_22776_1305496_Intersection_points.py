# -*- coding: utf-8 -*-
#python3.7
"""
- We will find the intersection points between f(t) and g(t)
"""
import numpy as np 
#from scipy.optimize import fsolve
import matplotlib.pyplot as plt 

########################## Function defining ##################################
def f_t( t):
    return 1.1*(t - 2.5)**2
def dfdt(t):
    return 2*1.1*(t-2.5)
    
def g_t( t):
    return 5*t + 2.5
def dgdt(t):
    return 5
def Newtons(f_t, df_dt,x0):
    eps = 1e-6
    i   = 0 
    N   = 100
    xn  = float(x0)
    while abs(f_t( xn)) > eps and i < N:
        x_next = xn - f_t(xn)/dfdt(xn)
        print(i , "fct_value", abs(f_t(xn)), x_next)
        xn = x_next
        i += 1
    if abs(f_t(xn)) < eps:
        return x_next
    else : 
        return np.nan
    

def Newtons2(g_t, dg_dt,x0):
    eps = 1e-6
    i   = 0 
    N   = 100
    xn  = float(x0)
    while abs(g_t( xn)) > eps and i < N:
        x_next = xn - g_t(xn)/dgdt(xn)
        print(i , "g_t_value", abs(g_t(xn)), x_next)
        xn = x_next
        i += 1
    if abs(g_t(xn)) < eps:
        return x_next
    else : 
        return np.nan
    
############################  Parameters #####################################
x0 = -9
xmax, xmin = 10 , -10 
HW4_graph1 = 'data'
################          plotting     #############################
x_root_ft = Newtons(f_t, dfdt, x0)
x_root_gt = Newtons2(g_t, dgdt, x0)
x = np.linspace(xmax,xmin, 21)
plt.figure(1)
plt.plot(x, f_t(x),'k-', ms=2 )
plt.plot(x, g_t(x), 'r-', ms=2)
plt.plot([x_root_ft], [f_t(x_root_ft)], 'b*', ms=12)
plt.plot([x_root_gt], [g_t(x_root_gt)], 'g*', ms=12)
plt.plot([x_root_ft-x_root_gt], [f_t(x_root_ft) - g_t(x_root_gt)],'r*', ms= 12 )
plt.plot([xmin, xmax], [0,0], 'r--')
plt.grid(True)
plt.savefig(HW4_graph1)
plt.show()
 

