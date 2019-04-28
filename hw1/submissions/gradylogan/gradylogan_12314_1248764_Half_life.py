# -*- coding: utf-8 -*-
import math

# Script that displays amount of C14 leftover after 3 specific time intervals
T  = 5730.
t  = [1e4, 1e5, 1e6]
N0 = 100.

for i in range(0,3):
    N  = N0*(math.exp(-t[i]/T))
    print N, "grams after", t[i], "years" 
#==========================================================================
    
# Script for manual imput of variables
T  = input('Half Life of material = ')
t  = input('Elapsed time = ')
N0 = 100

N  = N0*(math.exp(-t/T))
print N, "grams after", t, "years"
#=====================================
