import numpy as np

def my_Newton(fct, df_dx, x0):
    """
        - implementation of Newton's method
        for solving f(x) = 0, when f'(x) is known
    """
    xn = float(x0)
    eps = 1e-5
    N = 20
    i = 0
    while abs(fct(xn)) > eps and i < N and (fct(x0**(xn+1)) - fct(x0**xn)) > 1e-6:
        x_next = xn - fct(xn)/df_dx(xn)
        print(i, 'fct_value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan
