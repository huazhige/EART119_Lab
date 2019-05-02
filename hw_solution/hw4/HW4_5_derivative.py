#python2.7
"""
    - compute the derivative of a measured position of a vertical object as a function of time
"""
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                                params
#===================================================================================
v0 = 7                   # Initial velocity in m/s
g  = 9.81                  # Acceleration of gravity
n  = 500
t  = np.linspace(0, 1, n)  # 2000 points in time interval
y  = v0*t - 0.5*g*t**2     # Generate all heights

file_out = 'data/HW4_vertTraj.txt'
#===================================================================================
#                                data I/O
#===================================================================================
np.savetxt(file_out, np.array([ t, y]).T, fmt = '%10.6f%10.6f', header = 't[s]      z(t) [m]')

mData = np.loadtxt( file_out).T
a_t, a_y = mData[0], mData[1]

dt    = a_t[1]-a_t[0]
a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)
#===================================================================================
#                                derivatives etc.
#===================================================================================
i = 1
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1

#===================================================================================
#                                plots
#===================================================================================
print "The largest height achieved was %f m" % (largest_height), ' at t =',t[i]
# We might also like to plot the path again just to compare
plt.figure()
plt.subplot( 311)
plt.plot( a_t, a_y)
plt.ylabel('Height (m)')
plt.grid( True)

plt.subplot( 312)
plt.plot( a_t[1:-1], a_vel)
plt.ylabel('Velocity (m/s)')
plt.grid( True)

plt.subplot( 313)
plt.plot( a_t[1:-1], a_acc)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s2)')
plt.ylim( -g - 5, -g+5)
plt.grid( True)
plt.show()
