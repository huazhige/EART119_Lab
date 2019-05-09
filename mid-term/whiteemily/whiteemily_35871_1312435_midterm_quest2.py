# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:55:14 2019

@author: emlowhit
"""

#=============================================================================
#                       IMPORTS
#=============================================================================
import numpy as np
import matplotlib.pyplot as plt


# prof fnc, using Optimize. didn't recognize module
import opt_utils as utils
#=============================================================================
#                       PARAMS
#=============================================================================
xmin, xmax = -10, 10
x0 = 5
#tolerance
tol = 1e-6
iIt = 20
tmin, tmax = -10, 25
testPlot = True

#=============================================================================
#                       FCTS
#=============================================================================
def fct1(x):
    return x**5 + (2/5)*x**2 - 2

def fct2(x):
    return np.exp(-x/10) + x

def fct3(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)

#=============================================================================
#                       ROOTS
#=============================================================================
secfct1 = utils.my_Secant(fct1, x0, x0+10, N = 40)
secfct2 = utils.my_Secant(fct2, x0, x0+10, N = 40)
secfct3 = utils.my_Secant(fct3, x0, x0+10, N = 100)


#=============================================================================
#                       PLOTS
#=============================================================================
if testPlot == True:
    a_x = np.linspace(xmin, xmax, 1000)
    plt.figure(2)
    plt.plot(a_x, fct1(a_x), 'b-', label = 'f1(x)')
    plt.plot(a_x, fct2(a_x), 'g-', label = 'f2(x)')
    plt.plot(a_x, fct3(a_x), 'r-', label = 'f3(x)')
    plt.plot([xmin, xmax], [0,0], '--')
    plt.plot([secfct1], [fct1(secfct1)], 'b*', mfc = 'w', ms =10)
    plt.plot([secfct2], [fct2(secfct2)], 'g*', mfc = 'w', ms =10)
    plt.plot([secfct3], [fct3(secfct3)], 'r*', mfc = 'w', ms =10)
    plt.xlabel('t')
    plt.ylabel('fnc values')
    plt.ylim(-10,10)
    plt.grid(True)
    plt.legend()
    plt.show()









