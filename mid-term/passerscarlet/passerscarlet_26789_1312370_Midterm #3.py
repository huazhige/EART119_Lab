#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
MIDTERM QUESTION 3

@author: scarletpasser
"""

import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#                               load data
#--------------------------------------------------------------------------

#import data
data = np.loadtxt('midterm_dydx.txt', skiprows = 1).T

#----------------------------------------------------------------------------
#                               variables 
#--------------------------------------------------------------------------


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
plt.plot(t, z)                   #function plot
plt.ylabel('function')

plt.subplot(312)
plt.ylabel('first deriv')        #first derivative plot
plt.plot(t[2::], dzdt)      

plt.subplot(313)
plt.ylabel('second deriv')       #second derivative plot
plt.xlabel('time')
plt.plot(t[2::], d2zdt2)    
plt.ylim(-15,15)


plt.savefig( 'Miterm #3 graph')
plt.show()