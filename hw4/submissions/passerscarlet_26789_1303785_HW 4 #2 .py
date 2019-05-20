#python2.7

"""
HW 4 #2

    - Find the crossover point(s) between two functions: f(t) and g(t) 
    and find their values at those points
    - Compare with crossover derived in class, week 2

@author: scarletpasser
"""

import numpy as np
import opt_utils as opt_utils
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#                           define variables 
#----------------------------------------------------------------------------
t0 = 2.5
c  = 1.1
A  = 5
t  = np.arange(-10, 11)

#----------------------------------------------------------------------------
#                           functions
#----------------------------------------------------------------------------

# the two functions we want to find the crossover of: f(t), g(t)
def f(t):
    return c*(( t - t0)**2)
    
def g(t):
    return A * t + t0

# A new function representing the differnce between our two functions (f(t)-g(t))
def F(t):
    return c*(( t - t0)**2) - (A * t + t0)

# derivatice of F(t), done with pen and paper 
def dFdt(t):
    return 2*c*t - 2*c*t0 - A  

#----------------------------------------------------------------------------
#               Find crossover # of crossover points (part A)
#----------------------------------------------------------------------------

'''
From this graph of the two functions in question,
we can see that there are two crossover points, and make 
guesses based off of where they might me. 

'''


plt.figure(1)
plt.plot(t, f(t))
plt.plot(t, g(t))
plt.show()

#----------------------------------------------------------------------------
#                Find crossover points (part B)
#----------------------------------------------------------------------------
#Using Newton's method function from opt_utils find the two crossover points

#Root one found with a guess closer to the lower bound
Root1 = opt_utils.my_Newton(F, dFdt, -10 , tol = 1e-4, N = 20)
#Root two found with a guess closer to the upper bound
Root2 = opt_utils.my_Newton(F, dFdt, 10 , tol = 1e-4, N = 20)

print "t at crossover 1 =", str(Root1), "f(t) at crossover 1 =", f(Root1), "g(t) at crossover 1 =", g(Root1)
print "t at crossover 2 =", str(Root2), "f(t) at crossover 2 =", f(Root2), "g(t) at crossover 2 =", g(Root2)

#----------------------------------------------------------------------------
#                Compare with previous assignment (Part C)
#----------------------------------------------------------------------------

Cross1 = 0.43521761 #crossover taken from the week 2 in class assignment 

# plot showing the two functions,
#a crossover from week two, and a crossover found in this assignment

plt.figure(2)
plt.plot(t, F(t))
plt.plot(Root1, 0, marker = 'o')
plt.plot(Cross1, 0, marker = 'o')

plt.savefig('HW 4 #2 graph')    #save figure

plt.show()

