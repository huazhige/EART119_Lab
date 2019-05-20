# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:51:41 2019

@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt

#files
file_in = 'HW4_vertTraj.txt'

vrt_traj = np.genfromtxt(file_in, skip_header = 1, usecols = (0, 1)).T
#df/dx using central difference
dt = 1/len(vrt_traj[0])
dfdx_vrt_traj = (vrt_traj[1][2::] - vrt_traj[1][0:-2])/(2*dt)

#second derivative using central difference
second_derivative = (vrt_traj[1][2::] - 2*vrt_traj[1][1:-1] + vrt_traj[1][0:-2])/(dt**2)



plt.plot(vrt_traj[0], vrt_traj[1], 'r--', label = 'f(z)')
plt.plot(vrt_traj[0][0:-2], dfdx_vrt_traj, 'k--', label = 'df/dz')
plt.plot(vrt_traj[0][0:-2], second_derivative, 'g-', label = 'd^2f/dz^2')
plt.grid(True)
plt.legend(loc = 'upper right')
