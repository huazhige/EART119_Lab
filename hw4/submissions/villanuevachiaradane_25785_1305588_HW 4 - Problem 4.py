#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                Function Definitions
# =======================================================
def f_x1(x):
    f = -x**5 + (1/3)*x**2 + (1/2)
    return f

def f_x2(x):
    f = (np.cos(x))**2 + 0.1
    return f

def f_x3(x):
    f = np.sin(x/3) + 0.1*(x + 5)
    return f

def secant(fct, x0, x1, tol = 1e-5, N = 20 ):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        dfdx = (fct(x1) - fct(x0))/(x1 - x0)
        x_next = x1 - fct(x1)/dfdx
        x0 = x1
        x1 = x_next
        print(i, 'Function value:', abs(fct(x1)), x_next)
        i += 1
    # check if solution converged
    if abs(fct(x1)) < tol:
        return x1
    else:
        return np.nan

# =========================2=============================
#                      Parameters
# =======================================================
x0 = -9

xmin1 = -10
xmax1 = 10

xmin2 = -3
xmax2 = 3

# =========================3=============================
#                     Find roots
# =======================================================
x_root1 = secant(f_x1, x0, x0 + 10)
x_root2 = secant(f_x2, x0, x0 + 10)
x_root3 = secant(f_x3, x0, x0 + 10)

# =========================4=============================
#                        Plots
# =======================================================
a_x1 = np.linspace(xmin1, xmax1, 1000)
a_x2 = np.linspace(xmin2, xmax2, 1000)

plt.figure(1)

plt.plot(a_x1, f_x1(a_x1), 'k-')
plt.plot([x_root1], [f_x1(x_root1)], 'b*', ms = 10)
plt.plot([xmin1, xmax1], [0, 0], 'r--')
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')

plt.figure(2)

plt.plot(a_x1, f_x2(a_x1), 'k-')
plt.plot([x_root2], [f_x2(x_root2)], 'b*', ms = 10)
plt.plot([xmin1, xmax1], [0, 0], 'r--')
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')

plt.figure(3)

plt.plot(a_x2, f_x3(a_x2), 'k-')
plt.plot([x_root3], [f_x3(x_root3)], 'b*', ms = 10)
plt.plot([xmin2, xmax2], [0, 0], 'r--')
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')

plt.show()


# In[ ]:




