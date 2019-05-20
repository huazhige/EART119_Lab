#python2.7
"""
HW 4 #5

    - Using the central difference method, find the velocity 
    (first derivative), and the acceleration (second derivative), 
    from given data of position and velocity
   
    - Create three subplots of position, velocity, and acceleration
    as a function of time

@author: scarletpasser
"""

import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#                          load data  
#----------------------------------------------------------------------------

data = np.loadtxt('HW4_vertTraj.txt', skiprows = 1).T

#----------------------------------------------------------------------------
#                      define variables 
#----------------------------------------------------------------------------

t = data[0]      #time
z = data[1]      #position
N = len(t)       #length of time vector
dt = t[1] - t[0] #delta t between time incriments 

#----------------------------------------------------------------------------
#                      compute velocity (dz/dt)
#----------------------------------------------------------------------------

#using the central difference formula compute velocity

dzdt = np.zeros( N)
dzdt = (z[2::] - z[0:-2])/(2*dt)  


#----------------------------------------------------------------------------
#                   compute acceleration (d2z/dt2)
#----------------------------------------------------------------------------

#using the central difference formula for second derivatives compute acceleration

d2zdt2 = (z[2::] - 2*z[1:-1] + z[0:-2])/(dt**2)

#----------------------------------------------------------------------------
#                               plots
#----------------------------------------------------------------------------
plt.figure()

plt.subplot(311)
plt.plot(t, z)              #postion plot
plt.ylabel('position')

plt.subplot(312)
plt.ylabel('velocity')      #velocity plot
plt.plot(t[2::], dzdt)      

plt.subplot(313)
plt.ylabel('acceleration')  #acceleration plot
plt.xlabel('time')
plt.plot(t[2::], d2zdt2)    
plt.ylim(-15,15)


plt.savefig( 'HW 4 #5 graph')
plt.show()

