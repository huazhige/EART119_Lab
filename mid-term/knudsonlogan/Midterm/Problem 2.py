# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:43:33 2019

@author: lsknudso
"""


import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#   Defining functions and Parameters
# =============================================================================
def a_x (x):
    return -x**5 +2/5.*x**2 - 2.

def b_x (x):
    return np.exp(-x/10.) + x 
    
def c_x (x):
    return 10 * np.sin(x/4.) + 0.1*(x+12.)

functions = [a_x, b_x, c_x]                #list of functions
fnc_names = ['a_x','b_x','c_x']            #list of functions in string format, for print statements

#approx range to search for zeros
a_min, a_max = -10, 10 
b_min, b_max = -10, 10
c_min, c_max = -5, 5
#

Zeros = [ np.linspace(a_min,a_max,20), np.linspace(b_min,b_max,20), np.linspace(c_min,c_max,20)] #creates a vector for approximate zeros

###############################################################################
def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        x0 = x1
        x1 = x_next
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)
###############################################################################

# =============================================================================
# Calculation and Plotting
# =============================================================================

i = 0                                                                       #needed to select first function
for fn in functions:                                                        #Loop over functions
    z = []                                                                  #list of potential zeors
    for z0 in range (len(Zeros[i])):                                        #selects list of zero for function
        zero = Zeros[i][z0]                                                 #loop over particular zero 
        z0 = my_Secant(fn, zero, zero+.1)                                   #does the secant function
        if type(z0) == float:                                               #checks to see if the secant function output a value
            if np.round(z0, 3) in z:                                        #if the zero has already been found, go to the next
                False
            else:
                z.append(np.round(z0,3))                                    #if new zero, append it to list of zeros
    if len(z) == 0:                                                         #if no zeros were found, this lets the user know
        print("====================\nNo Zeros were found for %s"%(fnc_names[i]))
    else:
        print("====================\nZero(s) in %s at x = %s"%(fnc_names[i],z))       
                      
    plt.plot(np.linspace(-10,10,1000), fn(np.linspace(-10,10,1000)))        #plotting the function
    for cross in z:                                                         #plotting All found zeros
        plt.plot(cross, fn(cross), 'r*', ms = 10, )
    plt.legend(('%s'%(fnc_names[i]),'Zeros at x = %s'%(z)))                 #adding legend
    plt.savefig("Problem2%s"%(fnc_names[i]))                                #save fig
    plt.show()
    i += 1  


