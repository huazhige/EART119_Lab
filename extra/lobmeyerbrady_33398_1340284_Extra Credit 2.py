# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:49:21 2019

@author: Brady
"""
import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as inte
e= np.e
sin = np.sin
cos = np.cos


N= 1000.
xmin = 0.
xmax_f= np.pi
xmax_g= 1
x_f= np.linspace(xmin, xmax_f, N)
x_g= np.linspace(xmin, xmax_g, N)
def f(x_f):
    return sin(x_f)
def g(x_g):
    return 2*(x_g)*(e**((x_g)**2))

ia_fx= inte.trapezoidal(f, xmin, xmax_f, N)
ia_gx= inte.trapezoidal(g, 0, 1, 1000)

iact_fx = -cos(x_f)
iact_gx = (e**(x_g)**2)
print ia_fx
print iact_fx[999]
print ia_gx
print iact_gx[999]
plt.figure(1)
ax1= plt.subplot(211)
plt.plot(x_f, iact_fx, 'b')
plt.plot(x_f, f(x_f), 'r')
ax2= plt.subplot(212)
plt.plot(x_g, iact_gx, 'k')
plt.plot(x_g, g(x_g), 'g')
plt.show()