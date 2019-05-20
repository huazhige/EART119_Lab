"""
Lili Callahan
Homework #4

"""

#   Problem 5
"""
This problem uses position and time data to compute velocity and acceleration,
and then graphs each with respect to time.

"""

import numpy as np
import matplotlib.pyplot as plt

file1 = "HW4_vertTraj.txt"

#   load data
data1 = np.loadtxt(file1, skiprows = 1).T

#   define variables
t = data1[0]
z = data1[1]
N = len(t)
dt = t[1] - t[0]

#   calculate velocity

dfdt = np.zeros(N)

dfdt = (z[2::] - z[0:-2])/(2*dt)

#   calculate acceleration

d2fdt2 = np.zeros(N)

d2fdt2 = ((z[2::] - 2*z[1:-1] + z[0:-2])/(dt**2))

#   plotting
plt.subplot(311)
plt.ylabel('Position')
plt.plot(t, z)
plt.subplot(312)
plt.ylabel('Velocity')
plt.plot(t[2::], dfdt)
plt.subplot(313)
plt.ylabel('Acceleration')
plt.xlabel('Time')
plt.plot(t[2::], d2fdt2)
plt.ylim(-15, 15)
plt.savefig('5_graph')
plt.show()




