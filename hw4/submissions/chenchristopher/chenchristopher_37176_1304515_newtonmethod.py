# -*- coding: utf-8 -*-
#python 2.7

def my_Newton(fct, df_dx, x0):
    """
    implementation of Newton's method for solving for roots when f'(x) is known
    """
    i = 0
    xn = float(x0)
    eps = 1e-6
    while abs(fct(xn - fct(xn) / df_dx(xn)) - fct(xn)) > eps:
        x_next = xn - fct(xn) / df_dx(xn)
        print(i, 'fct_value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    return x_next