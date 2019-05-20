# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:16:41 2019
Homework 4 Problem 5
@author: Benny Quiroz
"""
import numpy as np
import matplotlib.pyplot as plt
import os 
import modules.opt_utils as ou

path = 'C:\\Users\\benit\\Python Scripts\\HW4'
os.chdir(path)
file_in = 'HW4_vertTraj.txt'
pos = np.loadtxt(file_in, comments = '#').T

vel = np.array([np.zeros(len(pos[0]) - 2), np.zeros(len(pos[0]) - 2)])
for i in range(1, len(pos[1]) - 1):
    vel[0][i-1] = pos[0][i-1]
    deltat = pos[0][i+1] - pos[0][i-1]
    vel[1][i - 1] = (pos[1][i+1] - pos[1][i-1])/(deltat)
    
acc = np.array([np.zeros(len(vel[0]) - 2), np.zeros(len(vel[0]) - 2)])
for i in range(1, len(vel[1]) - 1):
    acc[0][i-1] = vel[0][i-1]
    deltat = vel[0][i+1] - vel[0][i-1]
    acc[1][i - 1] = (vel[1][i+1] - vel[1][i-1])/(deltat)
    
a = 0
for i in range(0, len(acc[1])):
    a += acc[1][i]
average_acc = a/len(acc[1])

plt.cla()
plt.figure(1)
plt.tight_layout()

plt.subplot(311)
plt.plot(pos[0], pos[1], 'b-')
plt.plot(pos[0], pos[0]*0, 'k-', label = 'z = 0 or the ground')
plt.xlabel('time')
plt.ylabel('height or z')
plt.legend()

plt.subplot(312)
plt.plot(vel[0], vel[1], 'g-')
plt.plot(pos[0], pos[0]*0, 'k-')
plt.xlabel('time')
plt.ylabel('velocity')

plt.subplot(313)
plt.plot(acc[0], acc[1], 'r-')
plt.plot(pos[0], pos[0]*0, 'k-')
plt.xlabel('time')
plt.ylabel('acceleration')
average_a = 'The average acceleration is %.6f. ' %(average_acc)
text2 = 'If you will notice, this is a great approximation of the acceleration due to gravity.'
plt.text(0, -5, average_a)
plt.text(0, -6, text2)

plt.show()