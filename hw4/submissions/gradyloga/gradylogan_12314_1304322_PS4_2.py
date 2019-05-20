# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#==============================================================
# Constants
#==============================================================\
x0 = 2.5
t0 = 2.5
c  = 1.1
A  = 5
t = np.linspace(-10, 10, 1000)
#==============================================================
# Functions
#==============================================================
def ft(t):
    return c*(t-t0)**2

def gt(t):
    return (A*t) +t0

def dfdt(t):
    return 2*c*t-2*c*t0

def dgdt(A):
    return A

def minus(t):
    return ft(t)-gt(t)

def dminus(t):
    return dfdt(t)-dgdt(A)

   
 
root1 = opt_utils.my_Newton(minus, dminus, -10, tol = 1e-4, N =20)
root2 = opt_utils.my_Newton(minus, dminus, 10, tol = 1e-4, N =20)

#opt_utils

#=========================================================================
# Plots
#=========================================================================

plt.figure()
plt.plot(t, ft(t), 'r-')  
plt.plot(t, gt(t), 'b')
#k- is a black line. The other letters are just the colors
plt.plot([root1], [ft(root1)], 'r*', ms = 20 )
plt.plot([root2], [ft(root2)], 'b*', ms = 20 )
# ms is the size of the stars
plt.show()

print "t at crossover 1 =", str(root1), "f(t) at crossover 1 =", ft(root1),
"g(t) at crossover 1 =", gt(root1)

print "t at crossover 2 =", str(root2), "f(t) at crossover 2 =", ft(root2),
"g(t) at crossover 2 =", gt(root2)