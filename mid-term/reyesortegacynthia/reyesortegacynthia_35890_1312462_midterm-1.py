# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:23:00 2019

@author: creyesor
"""

import numpy as np
import matplotlib.pyplot as plt

def func_L( a, T, B): #DEFINING THE FUNCTION OF l AND IT'S VARIABLES
    return a*T**B #a represents alpha
#a = np.alpha()
#alpha = a

T = np.array( 1) #from first list, starts at zero
L = np.array( 3)

xmin, xmax = 10, 1000 #sets range
file_out = 'star_luminos.txt' #gets file and data in file

plt.figure()
ax.set_ylabel( 'Luminosity')
ax.set_xlabel( 'temperature')
plt.plot 
plt.ylim( -10,10)
plt.xlim( -10, 1000)

plt.show()