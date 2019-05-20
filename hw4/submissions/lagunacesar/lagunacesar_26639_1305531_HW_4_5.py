# -*- coding: utf-8 -*-
#python 3.6
import numpy as np
import matplotlib.pyplot as plt

dt = .1
ax = np.linspace(-10, 10, 500)
file_vert = 'HW4_vertTraj.txt'
vert_tra  = np.loadtxt(file_vert).T

t_s = vert_tra[0]
z_m = vert_tra[1]

#Central difference
dfdt_CD = z_m/t_s
secon_der = z_m/t_s**2
#dfdt_Cd = 
plt.figure()
plt.plot(ax, z_m) #postion
plt.figure()
plt.plot(ax, dfdt_CD, 'r-', ms = 3) #velocity
plt.figure()
plt.plot(ax, secon_der, 'b-', ms = 3) #acceleration
