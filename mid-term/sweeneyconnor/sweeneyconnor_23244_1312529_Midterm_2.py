# -*- coding: utf-8 -*-
"""
Midterm #2
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as ou

data_out = 'Midterm_2_plot.png'

xmin, xmax = -10, 10
x0         = 5
N          = 20
err        = 1e-5

#Define functions
def f1(x):
    return x**5 + (2/5)*x**2 - 2
def f2(x):
    return np.exp(-x/10) + x
def f3(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)

#Find roots
fsec_1 = ou.my_Secant( f1, x0, x0 + 10, err, N)
print fsec_1
fsec_2 = ou.my_Secant( f2, x0, x0 + 10, err, N)
print fsec_2
fsec_3 = ou.my_Secant( f3, x0, x0 + 10, err, N)
print fsec_3


#plot
plt.figure()
plt.subplot(111)

ax = np.linspace( xmin, xmax, 1000)
plt.plot( ax, f1( ax),  'k-', label = 'f1(x)')
plt.plot( ax, f2( ax),  'g-', label = 'f2(x)')
plt.plot( ax, f3( ax),  'r-', label = 'f3(x)')
plt.ylabel( 'f(x)')
plt.xlabel( 'x')
plt.legend()
plt.savefig('data_out')
plt.show()

