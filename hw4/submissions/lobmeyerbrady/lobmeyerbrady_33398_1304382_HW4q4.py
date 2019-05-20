# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:28:19 2019

@author: Brady
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

x= np.linspace( -10, 10, 100)

def fx1(x):
    return (((-x)**5)+((x**2)/3.)+.5)
def fx2(x):
    return ((np.cos(x))**2)+.1
def fx3(x): 
    return ((np.sin(x/3.))+.1*(x+5))

a_fx1= fx1(x)
a_fx2= fx2(x)
a_fx3= fx3(x)

plt.subplot(211)
plt.plot(x, a_fx1, 'r-')
plt.subplot(212)
plt.plot(x, a_fx2, 'g-')
plt.plot(x, a_fx3, 'b-')
root1= opt.my_Secant(fx1, -5.0, 5.0, tol=1e-4, N=20)
root2= opt.my_Secant(fx2, -5.0, 5.0, tol=1e-4, N=20)
root3= opt.my_Secant(fx3, -5.0, 5.0, tol=1e-4, N=20)

#print('the roots of f1(x) are %.3f.')%(root1)
print('there are no roots of f2(x).')
print('the roots of f3(x) are %.3f.')%(root3)





