# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:49:31 2019
Extra Cradit Problem 3
@author: Benny Quiroz
"""

import numpy as np
import modules.integrate_utils as intu

def f(x, y):
    return np.sqrt(x**2 + y**2)

def fg(x, y):
    return 4 - (x**2 + y**2)


def w(x, y):
    return x*y**2

"""
I couldn't figure out any function that wouldn't give me this error when calling the integration function:
    The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
"""
def wg(x, y):
    a = np.zeros(len(x))
    for i in range(0, len(x)) :
        if (0 <= x[i] <= 2):
                if (0 <= y[i] <= 1.5):
                    a[i] = 1
                else:
                    a[i] = -1
        else:
            a[i] = -1
    return a   
    
#x = np.array([-1, 1, -2, 2])
#y = np.array([-1, 1, -0.5, 0.5])
#sel = wg(x, y) >= 0

#print(wg(x, y))

fInt = intu.monteCarlo_vec(f, fg, -2.0, 2.0, -2.0, 2.0, 1000)
#Commented because of the error.
#wInt = intu.monteCarlo_vec(w, wg, -2.0, 2.0, -2.0, 2.0, 1000)

"""
Exact solution to f(x):
    Int = 2pi*Int(   (((r^2)^0.5)*r), r, 0, 2   )
    Int = 2pi*(8/3)
    Int = 16pi/3
"""
fVal = 16*np.pi/3
peF = abs((fInt - fVal) /fVal)*100

L1 = "The percent error of the MonteCarlo method for f(x. y) is %.5f percent." %(peF)
print(L1)