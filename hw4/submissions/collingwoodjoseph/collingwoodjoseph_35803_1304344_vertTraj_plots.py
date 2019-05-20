# -*- coding: utf-8 -*-
"""
HOMEWORK 4 QUESTION 5
"""
import matplotlib.pyplot as plt
import numpy as np
import os

data_dir = './'
traj_data = 'HW4_vertTraj.txt'
os.chdir(data_dir)

vertTraj = np.genfromtxt(traj_data, skip_header = 1).T
t,z = vertTraj[0], vertTraj[1]
delta_t = t[1::] - t[0:-1]

#Determines first and second derivatives
dz_dt = (z[2::]-z[0:-2])/(2*delta_t[1::])
d2z_dt2 = (z[2::]-2*z[1:-1]+z[0:-2])/(delta_t[1::])**2

#Plots z(t),dz/dt,d2z/dt2
f, ax = plt.subplots(3, sharex = True)

ax[0].plot(t,z)
ax[1].plot(t[0:-2],dz_dt)
ax[2].plot(t[0:-2],d2z_dt2)

plt.savefig( '4e')
