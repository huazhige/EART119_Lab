#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                Function Definitions
# =======================================================
# Part A Function
def f_x1(x):
    f = x**5 + (2 / 5)*x**2 - 2
    return f

# Part B Function
def f_x2(x):
    f = np.exp(-x / 10) + x
    return f

# Part C Function
def f_x3(x):
    f = 10*np.sin(x / 4) + 0.1*(x + 12)
    return f

# Function for using the Secant Method
def secant(fct, x0, x1, tol = 1e-5, N = 20 ):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        dfdx = (fct(x1) - fct(x0))/(x1 - x0)
        x_next = x1 - fct(x1)/dfdx
        x0 = x1
        x1 = x_next
        i += 1
    if abs(fct(x1)) < tol:
        print('Root:', x_next)
        return x1
    else:
        return np.nan

# =========================2=============================
#                      Parameters
# =======================================================
# Dependent value
x0 = -9

# Independent value range
xmin = -10
xmax = 10

# =========================3=============================
#                     Find roots
# =======================================================
# Finding the roots using the Secant Method
x_root1 = secant(f_x1, x0, x0 + 10)
x_root2 = secant(f_x2, x0, x0 + 10)
x_root3 = secant(f_x3, x0, x0 + 10)

# =========================4=============================
#                        Plots
# =======================================================
a_x1 = np.linspace(xmin, xmax, 1000)

## Plotting Part A
plt.figure(1)
# Part A's main function
plt.plot(a_x1, f_x1(a_x1), 'k-')
# x = 0
plt.plot([xmin, xmax], [0, 0], 'r--')
# Plotting the roots
plt.plot([x_root1], [f_x1(x_root1)], 'b*', ms = 10)
# Grid formatting
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')
plt.title("Part A Root")
plt.savefig('Problem 2 Part A')

## Plotting Part B
plt.figure(2)
# Part B's main function
plt.plot(a_x1, f_x2(a_x1), 'k-')
# x = 0
plt.plot([xmin, xmax], [0, 0], 'r--')
# Plotting the roots
plt.plot([x_root2], [f_x2(x_root2)], 'b*', ms = 10)
# Grid formatting
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')
plt.title("Part B Root")
plt.savefig('Problem 2 Part B')

## Plotting Part C
plt.figure(3)
# Part B's main function
plt.plot(a_x1, f_x3(a_x1), 'k-')
# x = 0
plt.plot([xmin, xmax], [0, 0], 'r--')
# Plotting the roots
plt.plot([x_root3], [f_x3(x_root3)], 'b*', ms = 10)
# Grid formatting
plt.grid(True)
plt.ylabel('Function Values f(x)')
plt.xlabel('x')
plt.title("Part C Root")
plt.savefig('Problem 2 Part C')

# Show the plots
plt.show()


# In[ ]:




