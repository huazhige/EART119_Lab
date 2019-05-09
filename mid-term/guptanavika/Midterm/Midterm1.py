
import math
import numpy as np
import matplotlib.pyplot as plt


data  = np.genfromtxt('star_luminos.txt', dtype=float).T





print ("a=8.61 b=0.2")


plt.figure()
plt.subplot()

plt.plot(data[0], data[1], 'b-')

plt.xlabel( 'Temperature [degree C]')
plt.ylabel( 'Luminosity [solar units]')
plt.title('Midterm Problem 1')
plt.show()