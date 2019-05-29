# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:24:04 2019

@author: Brady Lobmeyer
Extra Credit assignment #1

"""

import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as inte
e= np.e
sin = np.sin
cos = np.cos

def f(t):
    return 3*(t**2)*(e**(t**3)) 
t= inte.trapezoidal(f, 0, 1, 100)
print t

x= inte.midpoint(f, 0, 1, 100)
print x
print (e**(1**3))-(e**(0**3))
#=====================
# #2
#=======================

N= 1000
xmin = 0
xmax_f= np.pi
xmax_g= 1
x_f= np.linspace(xmin, xmax_f, N)
x_g= np.linspace(xmin, xmax_g, N)

a_fx= sin(x_f)
a_gx= 2*(x_g)*(e**((x_g)**2))

ia_fx= inte.trapezoidal(a_fx, 0.0, np.pi, 100)
#ia_gx= inte.trapezoidal(a_gx, 0, 1, 1000)

iact_fx = -cos(np.pi)+cos(0)
iact_gx = (e**(1)**2)-1
#print ia_fx
print iact_fx
#print ia_gx
print iact_gx
