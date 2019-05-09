# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:22:44 2019

@author: colli
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#Question 1
#==============================================================================
file_in='star_luminos.txt'
#load txt
L=np.genfromtxt(file_in, skip_header=1, usecols=0, dtype=float).T
temp=np.genfromtxt(file_in, skip_header=1,usecols=1, dtype=float).T

for i in temp:
    if i>10 and i<1000:
        temp=i
        print temp
    else:
        temp=False
        
        while temp!=False:
            ############plotting######
            plt.figure(1)
            plt.plot( temp, L,  'b-')
            plt.xlabel('temp. [degrees C]')
            plt.ylabel('luminosity[solar units]')
            plt.title('Luminosity vs temp')
            
plt.savefig('Question_1.png')






