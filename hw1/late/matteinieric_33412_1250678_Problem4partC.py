"""
Astr-119
Homework 1
problem 4: Program to detemrine how much
of an element is left using half life equation
"""
# alwyas important ===========================
import numpy as np

# Constants ===================================
N_0 = float( raw_input("How much of the substance did we start with? (if unknow, put 0)"))
tau = float( raw_input("What is the half life of the substance?"))
t   = float( raw_input("How much time has passed?"))
Exp = np.exp((-t)/tau)
# equation ===================================
N = N_0*(Exp)

if N_0 == 0 :
    print("%2f N_0 is left"%Exp)
else :
    print("%2f is left"%N)
