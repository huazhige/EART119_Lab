"""
Lili Callahan
Midterm Problem 3

"""

import numpy as np
import matplotlib.pyplot as plt

#############################################################################
#       Load Data
#############################################################################

file_in = "midterm_dydx.txt"
data = np.genfromtxt(file_in, skip_header = 1).T

#############################################################################
#       Computing Derivatives
#############################################################################

# define variables
t = data[0]
z = data[1]
N = len(t)
dt = t[1] - t[0]

# calculate velocity
dfdt = np.zeros(N)

dfdt = (z[2::] - z[0:-2])/(2*dt)

# calculate acceleration
d2fdt2 = np.zeros(N)

d2fdt2 = ((z[2::] - 2*z[1:-1] + z[0:-2])/(dt**2))

#############################################################################
#       Plotting
#############################################################################

plt.subplot(311)
plt.ylabel('Position')
plt.plot(t, z)
plt.subplot(312)
plt.ylabel('Velocity')
plt.plot(t[2::], dfdt)
plt.ylim(-15, 15)
plt.subplot(313)
plt.ylabel('Acceleration')
plt.xlabel('Time')
plt.plot(t[2::], d2fdt2)
plt.ylim(-15, 15)
plt.savefig('mt_3_plot')
plt.show()