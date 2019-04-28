"""
Astr-119
Homework 1
problem 4: Program to detemrine how much
of an element is left using half life equation
"""
# alwyas important ===========================
import numpy as np

# Constants ===================================

tau = 5750
t_10k = 10000
t_100k= 100000
t_1M  = 1000000
t_arr = np.array([10000, 100000, 1000000])
N10 = np.exp((-t_10k)/tau)
N100 = np.exp((-t_100k)/tau)
N1M = np.exp((-t_1M)/tau)
# equation ===================================
#for i in t_arr:
    #Frac = np.exp((-i)/tau)
    #print("Percentage of Carbon left", Frac)

print("Percentage of carbon left after 10k years", N10)
print("Percentage left after 100k years", N100)
print("Percentage left after 1M years", N1M)
