# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:45:35 2019

@author: creyesor
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

def fct1( x):
    return x**5 + 2/5*x**2 - 2
#def fct2( x):
    #return **(-x)/10 + x
def fct3( x):
    return 10*np.sin(x/4) + 0.1*(x + 12)
x0 = -10

tmin, tmax = -10, 10
#plt.plot( 'fct1', 'g-')
#plt.plot( 'fct3', 'k-')
a_x = np.linspace( xmin, xmax, 1000)
plt.ylim( -10,10)
plt.xlim( -10,10)
#plt.ylim(-30,30)
plt.plot( [xmin, xmax])
plt.legend()

