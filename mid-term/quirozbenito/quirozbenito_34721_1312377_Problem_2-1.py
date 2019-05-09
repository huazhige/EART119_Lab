# -*- coding: utf-8 -*-
"""
Benny Quiroz 
1680808
Problem 2
"""

import numpy as np
import matplotlib.pyplot as plt

def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    """
    From opt.utils
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        #print (i, abs( fct( x1)), x_next)
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)
    
#These are the given functions
def a_(x):
    return x**5 + (2/5)*x**2 -2
def b_(x):
    return np.exp(-1*x/10) + x
def c_(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)

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
#Allows us to see the area of intersection clearly.
plt.ylim(-2,2)
plt.legend()

#Guesses based on looking at the graph, but they shouldn't matter since each only
#Has one root. 
asect = my_Secant(a_, 0.5, 1)
bsect = my_Secant(b_, -1, -2)
csect = my_Secant(c_, -2, -3)

#PLotting each of the points as black dots.
plt.plot(asect, a_(asect), 'ko', ms = 3)
plt.plot(bsect, b_(bsect), 'ko', ms = 3)
plt.plot(csect, c_(csect), 'ko', ms = 3)
#Adding in a legend of sorts. It's just text but it works perfectly fine.
legend1 = 'a-root= (%.3f , %.3f)' %(asect, a_(asect))
legend2 = 'b-root= (%.3f , %.3f)' %(bsect, b_(bsect))
legend3 = 'c-root= (%.3f , %.3f)' %(csect, c_(csect))
plt.text(2.5, -0.5, legend1)
plt.text(2.5, -1.0, legend2)
plt.text(2.5, -1.5, legend3)

plt.show()
