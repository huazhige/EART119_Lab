# -*- coding: utf-8 -*-

import numpy as np

def my_Newton( fct, df_dx, x0):
    """
    implementation of newton's method for solving f(x)= 0 when f'(x) is known
    """
    xn = float(x0)
    eps = 1e-5
    N = 20
    i = 0
    while abs( fct( xn**(i + 1)) - fct( xn**i)) > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        print( i, 'fct value', abs( fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs( fct( xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan
