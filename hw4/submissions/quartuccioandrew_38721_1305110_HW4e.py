#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:11:20 2019

@author: andrewquartuccio
"""

import numpy as np
import matplotlib.pyplot as plt

data_in = './Data/HW4_vertTraj.txt'

mData = np.loadtxt(data_in).T
t = mData[0,:]
z = mData[1,:]
dt = mData[0,1] - mData[0,0] 
a_t = z/t
N = 1


def ode_FE(mData, a_t, dt, N):
    N_t = int(round(float(N)/dt))
    u = np.zeros(N_t+1)
    t = mData[0, :]
    u[0] = 0
    for n in range(N_t):
        u[n+1] = u[n] + dt*a_t[n]
    return u, t

u, t = ode_FE(mData, a_t, dt, N)



plt.figure(1)
plt.subplot(211)
plt.plot(t, mData[1,:],'b-')

