# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:19:29 2019
Extra Credit Problem 1
@author: Benny Quiroz
"""

import numpy as np
import modules.integrate_utils as intu

#Our function
def f(t):
    return (3*t**2)*np.exp(t**3)

#Our vaule given the 2 approximation methods. 
trap = intu.trapezoidal(f, 0, 1, 1000)
mid  = intu.midpoint(f, 0, 1, 1000)

"""
The actual value is given by:
    f(t) = 3t^2(e^t^3)
    F(t) = e^t^3
    Int = F(1) - F(0)
    Int = e^1^3 - e^0^3
    Int = e - 1
"""

aval = np.e - 1.0

#Percent error for both methods
peTrap = abs(((trap - aval)/aval)*100)
peMid  = abs(((mid - aval)/aval)*100)

stat = "The percent error of the trapezoid method is %.6f percent whereas the percent error of the midpoint method is %.6f percent."%(peTrap, peMid)
print(stat)