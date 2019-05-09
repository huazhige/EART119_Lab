# -*- coding: utf-8 -*-

#imports
import numpy as np
import matplotlib.pyplot as plt

#===================
#   varibales
#===================

Data = np.loadtxt('midterm_dydx.txt').T
t = Data[0,:]
z = Data[1,:]
N = len(t)
dt = t[1]-t[0] #assume its equidistand
dt = float(dt)

#=====================
#  calculations
#=====================
#derivative
dzdt = []
tt = []
for i in range(N-2):
    diff = z[i+2]-z[i]
    temp = diff/(2*dt)
    dzdt.append(temp)
    tt.append(t[i+1])


#second derivative, note that the equation in the lecture notes is wrong
ddzdtt = []
for i in range(N-2):
    diff = z[i+2]-2*z[i+1]+z[i]
    temp = diff/(dt**2)
    ddzdtt.append(temp)

#=====================    
#         plots
#=====================
im = plt.figure(1)
pIm1 = plt.subplot( 311)
plt.plot(t,z,'r')
plt.title('Position')
plt.xlabel('x')
plt.ylabel('y')

pIm2 = plt.subplot(312)
plt.plot(t[1:N-1],dzdt,'b')
plt.title('Velocity')
plt.xlabel('x')
plt.ylabel('dy/dt')

pIm3 = plt.subplot(313)
plt.plot(t[1:N-1],ddzdtt, 'g')
plt.title('Acceleration')
plt.xlabel('x')
plt.ylabel('d^2y/dt^2')
#the acceleration is mostly constant, ony small variances,
# probably due to the discretization

im.savefig('q3.png')