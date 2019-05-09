# imports
import numpy as np
import matplotlib.pyplot as plt

file_in = 'midterm_dydx.txt'

# parameters
Data = np.genfromtxt(file_in, skip_header = 1).T

x = Data[0]
y = Data[1]
dx = x[1]-x[0] # an approximation of the dx
vel = []
acc = []

# the for loop
for i in range(len(y)-1): #unsure why this is out of range/what to subtract it by to make it within range
    vel[i] = (y[i+1] - y[i-1])/(2*dx)
    acc[i] = (y[i+1] - 2*y[i] + y[i-1])/(dx**2)

# plotting
plt.figure(1)
plt.plot(x, y)
plt.plot(x, vel)
plt.plot(x, acc)
plt.savefig('Question3_fig.png')
plt.show()
