
"""
        Find the roots using the Secant method
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils


#ranges for each function 
time1 = np.linspace(-10,10,1000)
time2 = np.linspace(-10,10,1000)
time3 = np.linspace(-3,3,1000)


#------------------------------------------------------------------------------
#       first function
#------------------------------------------------------------------------------
def f1_x(x):
    return(-x**5 + (x**2)/3. + 0.5)
    
#plt.figure(1)
#plt.plot(time1, f1_x(time1), 'ro', ms = 2)
#plt.ylim(-1,1 ) #play with this range until the plot is precise
#plt.show()

root1 = opt_utils.my_Secant(f1_x, -1,1)
print('The root is: ',root1) 

#------------------------------------------------------------------------------
#       second function
#------------------------------------------------------------------------------
def f2_x(x):
    return (((np.cos(x))**2) + 0.1)

#plt.figure(2)
#plt.plot(time2, f2_x(time2), 'bo', ms = 2)
#plt.show()

root2 = opt_utils.my_Secant(f2_x, 0,1.2)
print('The root is: ',root2) 

#------------------------------------------------------------------------------
#       third function
#------------------------------------------------------------------------------
def f3_x(x):
    return (np.sin(x/3)+(0.1*(x+5)))

#plt.figure(3)
#plt.plot(time3, f3_x(time3), 'go', ms = 2)
#plt.show()

root3 = opt_utils.my_Secant(f3_x, -0.5,1.5)
print('The root is: ',root3) 

#------------------------------------------------------------------------------
#       MY ANSWERS : 1) 0.9577200035656286
#                    2) None
#                    3) -1.1767341257500834
#------------------------------------------------------------------------------