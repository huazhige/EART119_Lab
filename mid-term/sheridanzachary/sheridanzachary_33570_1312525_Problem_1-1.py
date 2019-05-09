# -*- coding: utf-8 -*-
"""
    -Problem 1:
        
"""
import numpy as np
import matplotlib.pyplot as plt
import os
#===================Load Data=================================================
data_dir = 'data'
data_file = 'star_luminos.txt'
os.chdir(data_dir)

lum_data = np.genfromtxt(data_file, skip_header = 1).T

#def fct(T):
#    L = alpha*T**beta
#===================Parameters================================================
Tmin, Tmax = lum_data[0][4071], lum_data[0][9854]
a_T = np.arange(Tmin, Tmax+1, dtype = float)




