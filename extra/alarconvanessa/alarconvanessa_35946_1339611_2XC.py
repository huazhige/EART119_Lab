# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:18:32 2019

python 3.7

@author: Nessa
"""

import numpy as np


#==================== functions ==============================================

def f_x (x):
    return np.sin(x)            #from 0 to pi

def g_x(x):
    return 2*x*np.exp(x**2)     #from 0 to 1

#================ discretize ==================================================
    
af_x = np.random.uniform( 0, np.pi, 1000)
ag_x = np.random.uniform( 0, 1, 1000 )


def mean(func, x):
    n = np.size(x)
    fvalues = 0
    for i in range(0, n):
        fvalues += func(x[i])
        i += 1
    mean = fvalues/n
    return mean

print('Mean of f(x): ', mean(f_x, af_x))
print('Mean of g(x): ', mean(g_x, ag_x))

#================ Integrals of functions ======================================

def intf_x(x):
    return -np.cos(x)

def intg_x(x):
    return np.exp(x**2)

integralf_x = intf_x(np.pi) - intf_x(0)
integralg_x = intg_x(1) - intg_x(0)

print('Integral of f(x) from 0 to pi: ', integralf_x)
print('Integral of g(x) from 0 to 1: ', integralg_x)


"""
Console output:
    
Mean of f(x):  0.6410641641121394
Mean of g(x):  1.6883587696986453
Integral of f(x) from 0 to pi:  2.0
Integral of g(x) from 0 to 1:  1.718281828459045

"""