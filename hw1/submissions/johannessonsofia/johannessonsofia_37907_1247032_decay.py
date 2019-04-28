# -*- coding: utf-8 -*-

"""
-program that computes radioactive decay using N = N0exp(-t/tau)

"""

import numpy as np

def decay(N_0, tau, t):
    """
    -calculates the remaining ammount of a radioactive substance
    input:
        N_0 = initial amount of nucleli, input 0 if you want the fraction
        tau = halflife 
        t = time elapes
    output:
        N = number of nucleai left after time t for a substance
        with halflife tau, returns precentage if no initial amount
        is given. The answer has 4 digits
    """
    if N_0 == 0:
        N_0 = 100
    
    N = N_0*np.exp(-t/tau)
    
    return N

#=============================
#    Cesium example
#=============================
    
tau = 5730;
t = [10000, 100000, 1000000]
fractions = []

for i in range(3):
    fractions.append( decay(0, tau, t[i]))
    print('fraction left after', t[i], 'years is', fractions[i], '%')