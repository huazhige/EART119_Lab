#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Assignment 1.4
by Lili Callahan

"""

#######################################################################
#   Problem 4
#   This problem computes the amount remaining of a radioactive
#   substance using its initial amount, half life, and
#   time elapsed
#######################################################################

#   a)

from math import e

#######################################################################
#   Parameters
#######################################################################

half_life = 5730                # Half life
t = 10000, 100000, 1000000      # Time

#######################################################################
#   Computations
#######################################################################

def quant(t, T, N0 = 1):
        return N0*e**(-t/T)
    
#   b)
    
#######################################################################
#   Computations
#######################################################################
        
for t in range(10000, 1000001):
    if t==10000 or t==100000 or t==1000000:
        print("Remaining amount is: " + str(quant(t, half_life)))
        
"""
If one wanted to give a value for N0, it would be put in the print line
after half_life. i.e, if N0 = 4:
        print("Remaining amount is: " + str(quant(t, half_life, 4)))
    
"""
        
#   c)
        
#######################################################################
#   Computations using user input
#######################################################################
        
T = int(raw_input("Half life: ")) 
t = int(raw_input("Time elapsed: "))

print("Remaining amount is: " + str(quant(t, T)))
