# -*- coding: utf-8 -*-
"""
*************************************Homework 1*********************************************
    Problem 4:
        Radioactive decay can be described by the following equation:
                                N =	N0exp(-t/tau)
    Where N is the quantity of the substance, tau is the half-life, and t is the elapsed time since a
    reference time t0.
        a) Write a python function that takes in the initial amount, time and half-life and
    returns the remaining amount. If no initial amount is given, the function should
    return the fractional amount remaining.
        b) 14C has a half-life of 5730 +/- 40 years. Write a script that writes out the fraction of
    14C that will remain after 10kyr, 100kyr, and 1Myr. Note that this is why 14
    C dating is not used for samples older than 100 kyr.
        c) Write a script that uses the same function, but this time the script computes the
    fraction of material remaining based on the user input for elapsed time and half-life
    of the substance. In python the function ‘input’ can be use to request a specific input
    for further calculations from the user of the program.
    
Annaconda 2, Python 2.7
"""

#============================================
#               Importing Packages
#============================================

import numpy as np

#============================================
#               Define Varriables
#============================================

#part B inputs
N0_c14 = 1 # value 1 gives fractional decay, can use " '' " instead
tau_c14 = 5730 # half life of C14
t_c14 = [1e5,1e6,1e7] # list of time decays

#Part C inputs 
print("Inputs For Part C:")
N0_C = raw_input(["Initial amount of sample (press enter for fractional amount)"]) 
t_C = raw_input(["Time of the decay"]) #time of decay
tau_C = raw_input(["Half life of material"]) #half life of material

#============================================
#               Calculation
#============================================

#============Part A===================
def rad_decay (N0,t,tau):
    if N0 == "":            #converts the empty string to 1 to get fractional amount left after decay
        N0 = 1
    N0 = float(N0) ; t= float(t) ; tau = float(tau) #converting inputs to floats
    return N0*np.exp(-t/tau)               #decay function



#============Part B====================
    
print("*************************\nPart B:\n")
for t_B in t_c14:
    print("Fraction of Carbon 14 remaining after %s years:\n%s\n"\
          %((t_B,rad_decay(N0_c14,t_B,tau_c14))))
#we cant use carbon dating afer 1M years becuase the fraction left is for all 
#intents and purposes is zero.
    
    
#============Parc C====================
    
print("*************************\nPart C:\n")
#this first if statement takes care of the case where fractional value left is disired
if N0_C == "": 
    print("Fraction Left with Time of Decay = %s and half life = %s:\n%s"\
          %(t_C, tau_C, rad_decay(N0_C,t_C,tau_C)))
#the else statement takes care of the case where the user inputs a starting amount of material
else:
    print("Ammount of Initial Material = %s\nTime of Decay = %s\nHalf life = %s\nMaterial left = %s\n"\
          %(N0_C,t_C,tau_C,rad_decay(N0_C,t_C,tau_C)))






