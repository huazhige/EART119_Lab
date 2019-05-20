#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                Function Definitions
# =======================================================
def f_t(t):
    t0 = 2.5
    c = 1.1
    f = c*(t-t0)**2
    return f

def dfdt(t):
    t0 = 2.5
    c = 1.1
    df =2*c*(t-t0)
    return df

def g_t(t):
    t0 = 2.5
    A = 5
    g = A*t + t0
    return g

def dgdt(t):
    t = 0
    A = 5
    return A

def Newton(function, d_dt, t0):
    """
    Implementation of Newton's Method
    for solving f(x) = 0 when f'(x) is known
    """
    t_next = 0
    tn = float(t0)
    abs_tn = abs(function(tn))
    eps = 1e-5 # epsilon to set bounds
    N = 20 # runs through 20 times
    i = 0
    while abs_tn > eps and i < N: # convergence criteria
        t_next = tn - function(tn)/d_dt(tn)
        print(i, 'Function value:', abs_tn, t_next)
        tn = t_next
        i += 1
    if abs_tn < eps:
        return t_next
    else:
        return np.nan

# =========================2=============================
#                      Parameters
# =======================================================
t0 = 2.5
# c = 1.1
# A = 5

tmin = -10
tmax = 10

# =========================3=============================
#                     Find roots
# =======================================================
tf_root = Newton(f_t, dfdt, t0)
tg_root = Newton(g_t, dgdt, t0)

# =========================4=============================
#                    Week 2 Method
# =======================================================
a_t = np.linspace(tmin, tmax, 1000)
eps = 0.1

a_ft = f_t(a_t)
a_gt = g_t(a_t)

sel = abs(a_ft - a_gt) < eps
print("Part A: There are two crossover points between -10 and 10.")
print("Part B & C: Crossover points at \n", "t =", a_t[sel], "\n", "g(t) =", a_ft[sel], "\n", "f(t) =", a_gt[sel])

# =========================5=============================
#                        Plots
# =======================================================
plt.figure(1)

plt.plot(a_t, f_t(a_t), 'k-')
plt.plot(a_t, g_t(a_t), 'k-')
plt.plot([tf_root], [f_t(tf_root)], 'r*', ms = 14)
plt.plot([tg_root], [g_t(tg_root)], 'b*', ms = 10)
plt.plot([tf_root - tg_root], [f_t(tf_root) - g_t(tg_root)], 'm*', ms = 12)
plt.plot([tmin, tmax], [0, 0], 'r--')

plt.grid(True)
plt.xlabel("t")
plt.ylabel('Function values f(t)')
plt.show()


# In[ ]:




