# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:12:29 2019

python 3.7

@author: Nessa
"""

import numpy as np
import integrate_utils as integrate

#========================= functions==========================================


def f_t (t):
    return (3*t**2)*np.exp(t**3)

def if_t(t):
    return np.exp(t**3)

#========= Trapezoidal and Midpoint Evaluation ================================

x0 = 0
xn = 1

time_intervals = np.arange(0, 1, 100)

trapf_t = integrate.trapezoidal( f_t, x0, xn, 100)  #trapezoidal method
midf_t = integrate.midpoint( f_t, x0, xn, 100)   #midpoint method

#real value of definite integral
realValue = if_t(xn) - if_t(x0)

print ('Integral using trapezoidal method: ', trapf_t)
print ('Integral using midpoint method: ', midf_t)
print ('Exact value of integral: ', realValue)

#=============== Error calc for both methods ==========

def errorCalc(real, approxValue):
    return (np.absolute(approxValue - real)/real)*100

trapError = np.round_(errorCalc(realValue, trapf_t), 2)
midError = np.round_(errorCalc(realValue, midf_t), 2)

print ( '\nPercent error for trapezoidal method\n', trapError, '%')
print ( 'Percent error for midpoint method\n', midError, '%')


"""
Console output:
    
Integral using trapezoidal method:  1.7186215916047791
Integral using midpoint method:  1.7181119551669362
Exact value of integral:  1.718281828459045

Percent error for trapezoidal method
 0.02 %
Percent error for midpoint method
 0.01 %
 
 
 """


