#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                   Importing File
# =======================================================

file = 'HW4_vertTraj.txt'
traj_data = np.loadtxt(file).T

# traj_data[0] = first column = time
# traj_data[1] = second column = position

# =========================2=============================
#                      Parameters
# =======================================================
# time increment
dt = .1
ax = np.linspace(-10, 10, 500)

# =========================3=============================
#                     Derivatives
# =======================================================
# central difference
dfdt_CD = traj_data[1] / traj_data[0]
df2dt2_CD = traj_data[1] / traj_data[0]**2

# =========================4=============================
#                       Plotting
# =======================================================
# initialize
plt.figure(1)

# position
plt.plot(traj_data[0], traj_data[1], 'r--')
plt.grid(True)
plt.savefig('Position')

# derivatives
plt.figure(2)
plt.plot(ax, dfdt_CD, 'b-')
plt.grid(True)
plt.savefig('Velocity')

plt.figure(3)
plt.plot(ax, df2dt2_CD, 'm-')
plt.grid(True)
plt.savefig('Acceleration')

# plot
plt.show()

