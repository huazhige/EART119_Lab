# -*- coding: utf-8 -*-
#python 2.7
"""
Calculates the amount of substance left using the radioactive decay formula
"""

import numpy as np

#=====================================================================================================
#Input variables
#=====================================================================================================
n0 = input('What is the initial amount of substance? Type 1 if you just want a fractional answer.')
t = input('How much time has elapsed?')
tau = input('What is the half-life?')

#=====================================================================================================
#Computation using radioactive decay formula N = N0 * e^(-t / tau)
#=====================================================================================================
def rad_decay(n0, t, tau):
    print("After " + str(t) + " years, " + str(n0 * np.e**(-t / tau)) + " remains.")
    
rad_decay(n0, t, tau)

#=====================================================================================================
#Runs the computation to find the amount of Carbon-14 left after 10ky, 100ky, and 1 My
#Uncomment to run
#=====================================================================================================
# =============================================================================
# rad_decay(1, 10000, 5730)
# rad_decay(1, 100000, 5730)
# rad_decay(1, 1000000, 5730) 
# =============================================================================
