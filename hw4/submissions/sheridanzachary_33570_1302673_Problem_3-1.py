# -*- coding: utf-8 -*-

import numpy as np

def my_Newton( fct, df_dx, x0):
    """
        - implementation of Newton's method for solving f(x) = 0,
        when f'(x) is known
    """
    x0 = float(x0)
    eps = 1e-6
    N = 20
    i = 0
    while (fct(x0**(i+1))-fct(x0**i)) > eps and i < N:
        x1 = x0 - fct( x0)/df_dx(x0)
        print( i, 'fct_value', (fct(x0**(i+1))-fct(x0**i)), x1)
        x0 = x1
        i += 1
    if (fct(x0**(i+1))-fct(x0**i)) < eps:
        return x1
    else: #solution did not converge
        return np.nan
    
