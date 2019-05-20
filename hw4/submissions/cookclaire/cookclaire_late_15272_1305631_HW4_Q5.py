# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:56:25 2019


"""
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = './'
file_in  = 'HW4_vertTraj.txt'

#===================================================================================
#                          load data
#===================================================================================
os.chdir( data_dir)

mData = np.genfromtxt( file_in, usecols=(0,1), skip_header=0).T
t, z = mData[0], mData[1]
h = 0.1

def dzdt(t):
    return (z(t+h) - (z(t - h)))/(2*h)
    

plt.figure(1)
ax = plt.subplot()
plt.plot(t, z, 'ro', label = "position")

#derivatives
ax.plot( t, dzdt(t), 'g', label = "velocity")




