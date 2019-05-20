# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:50:37 2019
Homework 4 Problem 4
@author: Benny Quiroz
"""
import numpy as np
import matplotlib.pyplot as plt
import modules.opt_utils as ou

def a_(x):
    return -1*x**5 + (1/3)*x**2 + 0.5
def b_(x):
    return (np.cos(x))**2 + 0.1
def c_(x):
    return np.sin(x/3) + 0.1*(x + 5)

"""
First let's graph them to get an idea of where to guess. 
"""
a_t = np.linspace(-10,10,1000)
plt.cla()
plt.figure(1)
plt.plot(a_t, a_(a_t), 'r-', label = 'a(x)') 
plt.plot(a_t, b_(a_t), 'g-', label = 'b(x)') 
plt.plot(a_t, c_(a_t), 'b-', label = 'c(x)')
plt.plot(a_t, a_t*0, 'k-') 
plt.xlim(-10,10)
plt.ylim(-2,2)
plt.legend()
plt.show()

#Guesses based on looking at the graph, but they shouldn't matter since each only
#Has one root. 
asect = ou.my_Secant(a_, 1, 1.5)
bsect = ou.my_Secant(b_, 0, 1)
csect = ou.my_Secant(c_, 1, 2)

print(asect, bsect, csect)

"""
This all looks good checking the graph. 
The function even works with b(x) which never crosses the x-axis. 
The answers are asect, bsect, and csect respectively. 
"""
