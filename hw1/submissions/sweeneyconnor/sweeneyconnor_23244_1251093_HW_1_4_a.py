# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 23:23:27 2019

@author: Connor
"""
import numpy as np

t0 = 0
N0 = input('What is the initial quantity of isotope? (in kg)')
t_lam = input('What is the half life of the isotope? (in years)')
t = input ('How much time has passed? (in years)')
N = N0*np.exp(-t/t_lam)

if N0 == "":
    print"Amount remaining: ", (N0)*100, "% of initial,", "or", N0, 'of initial.'

print "Amount remaining: ", (N/N0)*100, "% of initial,", "or", N/N0, 'of initial.'