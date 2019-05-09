# -*- coding: utf-8 -*-
"""
MIDTERM QUESTION 2
"""

import opt_utils
import numpy as np
import matplotlib.pyplot as plt

x_range = np.arange(-10,11)

#FUNCTION DEFINITIONS
def f1_x(x):
    return x**5.0 + (2.0/5.0)*x**2.0 - 2.0

def f2_x(x):
    return np.exp(-x/10.0) + x

def f3_x(x):
    return 10.0*np.sin(x/4.0) + 0.1*(x+12.0)

#FINDING THE ROOTS
for x in range(-10,11):
    roots_f1 = opt_utils.my_Secant(f1_x,x,x+.1)
    roots_f2 = opt_utils.my_Secant(f2_x,x,x+.1)
    roots_f3 = opt_utils.my_Secant(f3_x,x,x+.1)

#PLOTTTING
f, ax = plt.subplots(3)

for i in range(-10,11):
    ax[0].plot(i, f1_x(i), 'bo')
    ax[1].plot(i, f2_x(i), 'ko')
    ax[2].plot(i, f3_x(i), 'go')

#PLOTTING ROOTS
ax[0].plot(roots_f1,0,'rx', ms = 15)
ax[1].plot(roots_f2,0,'rx', ms = 15)
ax[2].plot(-0.463,0,'rx', ms = 15)

#STATING ROOTS IN LEGEND
ax[0].legend(['f1_x, root at x = 1.088'])
ax[1].legend(['f2_x, root at x = -1.118'])
ax[2].legend(['f3_x, root at x = -0.463'])