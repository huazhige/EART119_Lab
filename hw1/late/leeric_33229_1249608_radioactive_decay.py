# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:33:01 2019

@author: eric_
"""
import math
import sympy as sp

###############################################################
#               parameters
###############################################################
N0 = sp.Symbol("N0") #leaves initial amount as a variable
time = 5
half_life = 4
Upper_C14_half_life = 5730 + 40 #Upper-bound half-life of Carbon 14 isotope
Lower_C14_half_life = 5730 - 40 #Lower-bound half-life of Carbon 14 isotope
###############################################################
#               function
###############################################################
def decay(N0, t, tau):
    N = N0*(math.exp(-t/tau))
    return(N)
    
###############################################################
#               testing
###############################################################
    
print("If no initial amount, set N0 = N0. ")

#Carbon-14 Decay

print("Carbon-14 after 10kyr between: ", decay(N0, 1e4, Lower_C14_half_life), "and", decay(N0, 1e4, Upper_C14_half_life))
print("Carbon-14 after 100kyr between: ", decay(N0, 1e5, Lower_C14_half_life), "and", decay(N0, 1e5, Upper_C14_half_life))
print("Carbon-14 after 1Myr between: ", decay(N0, 1e6, Lower_C14_half_life), "and", decay(N0, 1e6, Upper_C14_half_life))

#===============================================================
#               User Input
#===============================================================
print("N = ", decay(N0, float(input("elapsed time: ")), float(input("half-life of substance: "))))
