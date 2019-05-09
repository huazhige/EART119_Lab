import matplotlib.pyplot as plt
import numpy as np
#data = np.genfromtxt("C:/users/ardas/downloads/star_luminos.txt", skip_header=1)
with open("C:/users/ardas/downloads/star_luminos.txt") as data:
    lines = data.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]    
'''
for i in data:
    i=np.split(i, 2)
    x=i[0]
    y=i[1]
print x
print y
'''
#plt.plot(x,y,"ko")
plt.figure(1)
#plt.set_xlim(10, 1000)
#plt.plot(x, y, "ko")
ax = plt.subplot()
ax.set_title("Temperature vs. Luminosity")
ax.legend( loc = 'upper right')
ax.set_xlabel('Temperature (Degrees Celsius)')
ax.set_ylabel('Luminosity (Solar Units)')
plt.show()
