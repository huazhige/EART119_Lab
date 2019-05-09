# -*- coding: utf-8 -*-
"""
- We wi;; ne taking the first and second derivative for the given data set
- we will the plot each derivative 
"""
import matplotlib.pyplot as plt
import numpy as np 
########################## Load data  ########################################
file_eq = "midterm_dydx.txt"
mData = np.loadtxt(file_eq).T
##########################   Derivatives ##########################
t_s = mData[0]  # time 
z_t = mData[1]  # distance in meters 
posi_T = z_t # this is position 
pos_t= z_t
dzdt_CD = z_t/t_s
ddzdtt = z_t/t_s**2
x= np.linspace(-10, 10, 500)
plt.figure(1)#position
plt.plot(x, dzdt_CD, 'k-', ms= 12)
plt.figure(2)#velocity 
plt.plot(x, ddzdtt, 'r-', ms = 12)
plt.figure(3)#acceleration 
plt.plot(x, pos_t, 'b-', ms= 12)
plt.show()