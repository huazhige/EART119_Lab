#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                      Parameters
# =======================================================
# Initial velocity
v0 = 7

# Gravity
g = 9.81

# Steps
n = 500

# Time
t = np.linspace(-3, 3, n)

# Trajectory equation
y = v0*t - 0.5*g*t**2 

# =========================2=============================
#                     Import File
# =======================================================
# Importing the data file and transposing it
data_file = "midterm_dydx.txt"
dydx_data = np.loadtxt(data_file).T

# Setting the time and vertical distance
a_t = dydx_data[0]
a_y = dydx_data[1]

# =========================3=============================
#                     Derivatives
# =======================================================
# Length of time
N = len(a_t)

# Time difference
dt = a_t[1] - a_t[0]

# Central Difference derivatives
a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)

# Set the zeros
a_vel = np.hstack( (0,a_vel, 0))
a_acc = np.hstack( (0,a_acc, 0))

# =========================4=============================
#                       Plotting
# =======================================================
plt.figure()

## Plotting the initial data
plt.subplot(311)
plt.plot(a_t, a_y)
# Grid formatting
plt.ylabel('Height [m]')
plt.grid(True)
plt.title("Derivatives")

## Plotting the first derivative: Velocity
plt.subplot(312)
plt.plot(a_t[1:-1], a_vel[1:-1])
# Grid formatting
plt.ylabel('Velocity [m/s]')
plt.grid(True)

## Plotting the second derivative: Acceleration
plt.subplot(313)
plt.plot( a_t[1:-1], a_acc[1:-1])
# Grid formatting
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s^2]')
plt.ylim(-g - 5, -g + 5)
plt.grid(True)

# Show the plots
plt.savefig('Problem 3')
plt.show()


# In[ ]:




