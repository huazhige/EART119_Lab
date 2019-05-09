# -*- coding: utf-8 -*-

""" 
- We will be ploting our data sets and the power-law fit 
"""
import numpy as np 
import matplotlib.pyplot as plt 
######################### Params ###############################################
xmin, xmax = 10, 1000
x= np.linspace( xmin, xmax, 100) # I assigned x for the value of T which is temperature 
######################### Function defenition #############################

###########################################################################
A = .5 #this is the value for Alpha 
b = 5 # this is the value for Beta
def luminosity(x):
    return A*x**b
print(luminosity)
########################## Load data  ########################################
file_eq = "star_luminos.txt"
mData = np.genfromtxt(file_eq, usecols = (0, 1)).T
########################## Plotting ###########################################
plt.figure(1)
plt.plot(x, luminosity(x), 'ko', ms = 3)
plt.ylabel('Temperature')
plt.xlabel('degree[c]')
plt.plot(mData, 'ro', ms = 3)
plt.grid(True)
plt.savefig()
plt.show(PartA_pic)
plt.show()