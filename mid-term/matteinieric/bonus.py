"""
hoping to get at least 1 point for importing numpy
"""

import numpy as np
import matplotlib.pyplot as plt


#===================================================================================
#                                params
#===================================================================================
useForLoop = False # switch between vectorized and for loop solution

v0 = 7                   # Initial velocity in m/s
g  = 9.81                  # Acceleration of gravity
n  = 500
t  = np.linspace(0, 1, n)  # 2000 points in time interval
# this is how the synthetic data is created, compare to example from week 1 and 2
# --> position of object on vectical trajectory with starting velocity v0
y  = v0*t - 0.5*g*t**2     # Generate all heights

file_in = 'midterm\midterm_dydx.txt'
#===================================================================================
#                                data I/O
#===================================================================================

# re-load synthetic data for demonstration purposes
mData = np.loadtxt( file_in).T
a_t, a_y = mData[0], mData[1]

#===================================================================================
#                                derivatives etc.
#===================================================================================
N        = len( a_t)
dt    = a_t[1]-a_t[0]

if useForLoop == True:# solve within for loop
    a_vel = np.zeros( N) # first and last elements cannot be compute with CD
    a_acc = np.zeros( N)

    for i in range( 1, N-1):
        a_vel[i] = ( a_y[i+1] - a_y[i-1])/(2*dt)
        a_acc[i] = ( a_y[i+1] - 2*a_y[i] + a_y[i-1])/(dt**2)
else: # vectorized solution
    a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
    a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)
    # add zeros at beginning and end for plotting purposes
    a_vel = np.hstack( (0,a_vel, 0))
    a_acc = np.hstack( (0,a_acc, 0))

# From Week 2:
i = 1
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1

#===================================================================================
#                                plots
#===================================================================================
t_maxHeight = a_t[i]
x = np.linspace(-3, 3+1, 6)
y = (-2*x)*(-3)*(np.exp(-(x)**2))
plt.subplot( 312)
# skip zeros and beginning and end
plt.plot( a_t[1:-1], a_vel[1:-1])
plt.plot(x,y)

plt.ylabel('Rate of Temp change')
plt.grid( True)
plt.show()
#plt.savefig('bonus.png')
