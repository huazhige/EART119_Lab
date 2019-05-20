#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def my_Newton(fct, df_dx, x0):
    """
    Implementation of Newton's Method
    for solving f(x) = 0 when f'(x) is known
    """
    x_next = 0
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 0
    while abs(fct(xn**(i+1))) - abs(fct(xn*(i))) > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        print(i, 'fct_value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else:
        return np.nan

