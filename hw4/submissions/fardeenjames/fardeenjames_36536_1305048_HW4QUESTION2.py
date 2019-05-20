import numpy as np
import matplotlib.pyplot as plt
import os
import opt_utils
tmin, tmax = -10, 10
t0 = 2.5
c = 1.1
A = 5


def fct_f_t(  t, c, t0):
    return c*(t - t0)**2

def df_dt( t, c, t0):
    return 2*c*(t - t0)

def fct_g_t(  t,A, t0):
    return A*t + t0

def dg_dt( t, A, t0):
    return A

def fct_h_t( t):
    t0 = 2.5
    c = 1.1
    A = 5
    return ((c*(t - t0)**2) - (A*t + t0))

def dh_dt( t):
    t0 = 2.5
    c = 1.1
    A = 5
    return (2*c*(t - t0) - A)
'''
def my_Newton( fct_h_t, dh_dt, t0):
    tn = float(t0)
    eps = 1e-5
    N = 20
    i = 0
    while abs(fct_h_t( tn, c, A, t0)) > eps and i < N:
        t_next = tn - fct_h_t( tn, c, A, t0)/dh_dt(tn, c, A, t0)
        print(1, 'fct_value', abs(fct_h_t(tn, c, A, t0)), t_next)
        tn = t_next
        i += 1
    if abs(fct_h_t( tn, c, A, t0)) < eps:
        return t_next
    else:
        return np.nan
'''   


t_root = opt_utils.my_Newton( fct_h_t, dh_dt, 5)
t_root2 = opt_utils.my_Newton( fct_h_t, dh_dt, 0)



a_t = np.linspace( tmin, tmax)
a_ft = fct_f_t( a_t, c, t0)
a_gt = fct_g_t( a_t, A, t0)
a_ht = fct_h_t( a_t)

plt.plot( a_t, fct_f_t(a_t, c, t0),    'r', label = 'f(t)')
plt.plot( a_t, fct_g_t(a_t, A, t0),    'b', label = 'g(t)')
plt.plot( [t_root], [fct_f_t(t_root, c, t0)], 'r*', ms = 10)
plt.plot( [t_root2], [fct_g_t(t_root2, A, t0)], 'r*', ms = 10)
# plt.plot( a_t, fct_h_t(a_t, c, A, t0), 'g', label = 'h(t)')


#plt.figure(2)
#plt.plot( a_ht, fct_h_t(a_t), 'k-')
#plt.plot( [t_root], [fct_h_t(t_root)], 'r*', ms = 14)
#plt.plot( [tmin, tmax], [0, 0], 'r--')
##plt.grid( True)
#plt.legend()
#plt.show()