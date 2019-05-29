# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:10:00 2019
Extra Credit Problem 2
@author: Benny Quiroz
"""

import numpy as np
import modules.integrate_utils as intu


def f(x):
    return np.sin(x)

def g(x):
    return 2*x*np.exp(x**2)

#Discretizing each function 
fx = np.random.uniform(0, np.pi, 1000)
fy = f(fx)
#Finding the average value
fave = fy.sum()/1000

gx = np.random.uniform(0, 1, 1000)
gy = g(gx)
gave = gy.sum()/1000

"""
For f(x):
    F(x) = -cos(x)
    Int = -cos(pi) - (-cos(0))
    Int = 2
For g(x):
    G(x) = exp(x**2)
    Int = exp(1**2) - exp(0**2)
    Int = e -1
"""

#Integrating using our midpoint method
fInt0 = intu.midpoint(f, 0, np.pi, 1000)
gInt0 = intu.midpoint(g, 0, 1, 1000)

"""
The average value should be for f(x):
    fave = fInt/(pi -0)
and for g(x):
    gave = gInt/(1 - 0)
    
Therefore by multiplying fave and gave by pi and 1 respectively
we can find a value of their integrals and compare them. 
"""
#Our values for the integral using the formula for average value backwards. 
fInt1 = fave*np.pi
gInt1 = gave*1

#Our actual values
fVal = 2.0
gVal = np.e - 1

#Just a text comparison
L1 = "Comparison of the integrals for both methods: average     midpoint      actual"
L2 = "                                              %.5f     %.5f       %.5f" %(fInt1, fInt0, fVal)
L3 = "Comparison of the integrals for both methods: average     midpoint      actual"
L4 = "                                              %.5f     %.5f       %.5f" %(gInt1, gInt0, gVal)

print(L1)
print(L2)
print(L3)
print(L4)



