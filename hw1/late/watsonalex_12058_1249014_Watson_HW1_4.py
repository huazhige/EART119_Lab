# -*- coding: utf-8 -*-
"""
                        Homework 1 Problem 4 (Bonus)
                                Alex Watson

    - write a radioactive decay function that:
        (a) takes in N0, t, & tau and finds N
        (b) finds the fraction of 14C after 10k, 100k, and 1Myr
        (c) find the fraction of a radioactive material based off of the user input for t and tau
"""
import numpy as np
import math
#==============================================================================
#                             Part A,B,C: Functions
#==============================================================================

# the function itself is the function for part a, while part b & c will utilize it

def rad_decay( t, tau, N0 = None):
    if N0 is None:
        N0 = 1
    N = N0*math.exp(-(t/tau))
    if N0 == 1:
        print 'fraction of material remaining:', N
    else:
        print 'amount of material remaining: %10.2f units'%(N)

#==============================================================================
#                              Part B: Parameters
#==============================================================================

t_b   = np.array([1e4, 1e5, 1e6])
tau_b = 5730

#==============================================================================
#                             Part B: Computations
#==============================================================================

print 'Part B: Carbon 14 Radioactive Decay'
for i in range( 3):
    rad_decay( t_b[i], tau_b)
    
#==============================================================================
#                              Part C: Parameters
#==============================================================================

print 'Part C: User Input'   
      
t_c   = float( raw_input( 'time elapsed (part c): '))
tau_c = float( raw_input( 'half-life (part c): '))

#==============================================================================
#                             Part C: Computation
#==============================================================================

rad_decay( t_c, tau_c)