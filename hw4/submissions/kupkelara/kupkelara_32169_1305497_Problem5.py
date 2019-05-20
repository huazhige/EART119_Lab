#!/usr/bin/env python
# coding: utf-8

# In[40]:





# In[27]:


#!python3

import numpy as np
import matplotlib.pyplot as plt
import os

"""Data increase in .002004 for time.
There's a funky bug in the code that I have no idea where it is from.
"""

dataTraj = np.loadtxt('HW4_vertTraj.txt',skiprows=1)#adjust to find proper location
time = np.ndarray.tolist(dataTraj[:,0])
meters = np.ndarray.tolist(dataTraj[:,1])
time2 = time[0:-1]


def der1_dataTraj(time, meters,h=1): #first derivative
    length = len(dataTraj)-1
    i = 0
    dmeters = []
    while i < length:
        holder = (meters[i+1]-meters[i-1])/(2*(h))
        i+=1
        dmeters.append(holder)
    return time, dmeters

def der2_dataTraj(time, meters,h=1): #2nd derivative
    length = len(dataTraj)-1
    i = 0
    dmeters = []
    while i < length:
        holder = (meters[i+1]-2*meters[i]+meters[i-1])/((h)**2)
        i+=1
        dmeters.append(holder)
    return time, dmeters

dx,dy = der1_dataTraj(time, meters, h= 0.002004 )
ddx,ddy = der2_dataTraj(time, meters,h= 0.002004)

plt.figure(2)
ax2 = plt.subplot( 111)
plt.plot(time, meters)
plt.show()

plt.figure(3)
ax2 = plt.subplot( 111)
plt.plot(time2, dy)
plt.show()

plt.figure(4)
ax2 = plt.subplot( 111)
plt.plot(time2,ddy)
plt.show()



# In[6]:


len(meters)
#time[499+1]-2*time[i]+time[499-1]


# In[76]:





# In[82]:





# In[33]:





# In[ ]:




