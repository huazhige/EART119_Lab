import numpy as np
import matplotlib.pyplot as plt


file_in = ('HW4_vertTraj.txt')

Data = np.genfromtxt(file_in, usecols = (0, 1), skip_header = 1).T

xlist = Data[0]
zlist = Data[1]
vellist = []
acclist = []

print(type(Data))
print(type(xlist))
print(type(zlist))

def x(t):
    return Data[0][t]

def z(t):
    return Data[1][t]

def vel(t):
    return (z(t+1)-z(t-1))/(2*0.002004)

def acc(t):
    return (vel(t+1)-vel(t-1))/(2*0.002004)

l = len(xlist)-2
for i in range(1, l):
    vellist.append(vel(i))
    if(i>2 and i!=l-1):
        acclist.append(acc(i))

plt.xlabel('Time (s)')
plt.plot(xlist, zlist, c = "black")
plt.plot(xlist[3:], vellist, c = "red")
plt.plot(xlist[6:], acclist, c = "yellow")
plt.savefig('pos&vel&acc.png')
plt.show()