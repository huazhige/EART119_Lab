import numpy as np
import integrate_utils as utils

def fct_f(r, Q):
    return r**2

def fct_g(r, Q):
    return r**2

def fct_w(x, y):
    return x*y**2

def fct_v(x, y):
    return 1

f_Int = utils.monteCarlo(fct_f, fct_g, 0, 2, 0, np.pi, 2000)
g_Int = utils.monteCarlo(fct_w, fct_v, 0, 2, 0, 1.5  , 2000)

print(f_Int)
print(g_Int)