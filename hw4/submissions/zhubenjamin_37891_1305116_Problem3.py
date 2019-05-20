# -*- coding: utf-8 -*-
"""
HW 4 problem 3
Benjamin Zhu 1696575
Pf. Tomas Goebel 
Astro/Earth 119

modify the function so that the iteration stops if
f(x + deltax) - f(x) is almost or is equal to zero.

I don't have the one from class, so I assume it is the same
as the one from opt_utils
"""

#=======================================================
#           function
#=======================================================

def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20, eps = 1e-6):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: 
        slopetest = df_dt( xn)
        if slopetest < eps:
            i += N
        else:
            x_next = xn - fct( xn)/df_dt( xn)
            print i, abs( fct( xn)), x_next
            xn = float( x_next)
            i += 1
    if abs( fct( xn)) > tol:
        return None
    else:
        return float( x_next)










