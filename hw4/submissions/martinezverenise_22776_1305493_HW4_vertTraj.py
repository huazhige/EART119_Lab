# -*- coding: utf-8 -*-
#python3.7
import numpy as np 
import matplotlib.pyplot as plt
file_eq = "HW4_vertTraj.txt"
mTraj = np.loadtxt(file_eq).T
t_s = mTraj[0]
z_m = mTraj[1]
pos_t= z_m
dzdt_CD = z_m/t_s
ddzdtt = z_m/t_s**2
x= np.linspace(-10, 10, 500)
plt.figure(1)#position
plt.plot(x, dzdt_CD, 'k-', ms= 12)
plt.figure(2)#velocity 
plt.plot(x, ddzdtt, 'r-', ms = 12)
plt.figure(3)#acceleration 
plt.plot(x, pos_t, 'b-', ms= 12)
plt.show()
