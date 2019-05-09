# imports
import numpy as np
import matplotlib.pyplot as plt

# file imports
file_in = 'star_luminos.txt'

# parameters
Data = np.genfromtxt(file_in, skip_header = 1).T

temp = Data[0]
luminosity = Data[1]


log_temp = np.log(temp)
log_lum = np.log(luminosity)

# plotting
plt.figure(1) # regular
plt.title('Temperature vs. Luminosity')
plt.plot(temp, luminosity)
plt.xlabel('Temperature (C)')
plt.ylabel('Luminosity (Solar Units)')
plt.savefig('Question1_fig1.png')
plt.show()

plt.figure(2) # power law
plt.title('Logarithmic Temperature vs. Logarithmic Luminosity')
plt.xlabel('Logarithmic Temperature (log(C))')
plt.ylabel('Logarithmic Luminosity (log(Solar Units))')
plt.savefig('Question1_fig2.png')
plt.plot(log_temp, log_lum)
plt.show()