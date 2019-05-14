# -*- coding: utf-8 -*-

import numpy as np

def ra_decay(halflife, t_elapsed, n_i=1):
    N = n_i*np.exp(-t_elapsed / halflife)
    return N

#parameters
halflife_c14 = 5730
t_elapsed = [10e3, 100e3, 1e6]

for n in t_elapsed:
    frac = ra_decay(halflife_c14, n)
    print(frac)
