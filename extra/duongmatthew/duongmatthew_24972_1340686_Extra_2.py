# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:48:22 2019
    - Calculates the mean and integral value of given functions over the same 
    given domains.
@author: maduong
"""

import numpy as np
### my modules
import integrate_utils as int_utils

#==============================================================================
#                                 fct definition
#==============================================================================
def f_x(x):                     # both functions defined
    return np.sin(x)
def g_x(x):
    return 2*x*np.exp(x**2)

#==============================================================================
#                                 parameters
#==============================================================================
xminf, xmaxf = 0, np.pi            # initial and final x values for f_x
xming, xmaxg = 0, 1                # initial and final x values for g_x
N = 1000

# function values for each x for both functions
a_fx = np.linspace( xminf, xmaxf, N) 
a_gx = np.linspace( xming, xmaxg, N)

#==============================================================================
#                                 compute integrals
#==============================================================================
# integrations using trapezoial method 
f_int = int_utils.trapezoidal(  f_x, xminf, xmaxf, N) 
g_int = int_utils.trapezoidal(  g_x, xming, xmaxg, N)  

#==============================================================================
#                                 compute means
#==============================================================================
# averages/means calculated
f_mean = np.mean(f_x(a_fx))
g_mean = np.mean(g_x(a_gx))

print ('mean value of f:   ', f_mean, 'integral value of f:   ', f_int)
print ('mean value of g:   ', g_mean, 'integral value of g:   ', g_int)
# note that the mean of f is 2/pi since the x domain was over pi while the integral was 2.

