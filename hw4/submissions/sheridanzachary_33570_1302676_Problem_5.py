# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os
#=====================load data===============================================
data_dir = 'data'
traj_file = 'HW4_vertTraj.txt'
os.chdir(data_dir)
traj_data = np.genfromtxt(traj_file, skip_header=2).T
#================parameters/function definitions==============================
a_t = traj_data[0]
a_z = traj_data[1]
z_max = max(a_z)
mz_id = np.arange(traj_data[0].shape[0])[traj_data[1] == z_max] 
t_maxz  = a_t[mz_id]

g = 9.81 #m/s**2
dt = 0.1
v0 = (z_max+0.5*g*t_maxz**2)/t_maxz #finding initial velocity to use in fct

def fct(t):
    return v0*t-0.5*g*t**2
def vfct(t):
    return v0 - g*t
#======================calculations===========================================
dzdt_CD = (fct(a_t+dt) - fct(a_t-dt))/(2*dt)    #velocity through CD appr.
dz2d2t_CD = (vfct(a_t+dt) - vfct(a_t-dt))/(2*dt)#acceleration through CD appr.
#==========================plotting===========================================
plt.figure(1)
ax1 = plt.subplot(3, 1, 1)
ax1.plot(a_t, fct(a_t), 'k-')
ax1.plot(a_t, np.linspace(0, 0, 499), 'r--')
plt.ylabel('position')
plt.grid(True)
ax2 = plt.subplot(3, 1, 2)
ax2.plot(a_t, dzdt_CD, 'b-')
ax2.plot(a_t, np.linspace(0, 0, 499), 'r--')
plt.ylabel('velocity')
plt.grid(True)
ax3 = plt.subplot(3, 1, 3)
ax3.plot(a_t, dz2d2t_CD, 'g-')
ax3.plot(a_t, np.linspace(0, 0, 499), 'r--')
plt.ylabel('acceleration')
plt.xlabel('time')
plt.grid(True)
plt.show()






