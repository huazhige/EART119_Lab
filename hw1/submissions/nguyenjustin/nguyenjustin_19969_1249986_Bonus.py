# -*- coding: utf-8 -*-
#Created by: Justin Nguyen
#Recent edit: 4/14/2019
"""
Given:
    N = N0**(-t/tau)
        N0 = quantity of the substance
        tau = half-life
        t = elapsed time since reference time t0
"""
import numpy as np
from fractions import Fraction
#==============================================================================
"""                                 Part A                                  
    Write a python function that takes in the initial amount, time 
    and half-life and returns the remaining amount. If no initial amount is
    given, the function should return the fractional amount remaining       """
#==============================================================================
N_0 = 0
t = 10
tau = 10

def analytic(N_0, t, tau):
    if N_0 == 0:
        return np.exp(-t / tau)
    else:
        return N_0 * np.exp(-t / tau)

print Fraction(analytic(N_0, t, tau))
print analytic(N_0, t, tau)
#==============================================================================
"""                                 Part B                                  
   14C has a half-life of 5730 +/- 40 years. Write a script that writes out 
   the fraction of 14C that will remain after 10kyr, 100kyr, and 1Myr. Note 
   that this is why 14C dating is not used for samples older than 100 kyr.  """
#==============================================================================
#tau = (5730 +/- 40)

#print tau



