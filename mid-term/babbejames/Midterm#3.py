#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:52:57 2019

@author: jtbabbe
"""

import numpy as np
import matplotlib.pyplot as plt

#=====================================================
#               load data
#=====================================================

data = np.genfromtxt('midterm_dydx.txt', comments = '#').T
t = data[0]
z = data[1]

#=====================================================
#               parameters
#=====================================================                     
dt = (t[1::] - t[0:-1])            
                     
                     
#=====================================================
#               fct def
#=====================================================
            
#   - CD Method
dzdt_CD = (z[2::] - z[0:-2])/(2*dt[1::]) 
d2zdt2_CD = (dzdt_CD[2::] - dzdt_CD[0:-2])/(2*dt[3::])                    
                     
#=====================================================
#               plot
#=====================================================           
          
plt.figure()
ax1 = plt.subplot(311)
ax1.plot(t, z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('f(t)')

ax2 = plt.subplot(312)
ax2.plot( t[:-2], dzdt_CD)
plt.grid(True)
plt.xlabel('t')
plt.ylabel("f'(t)")

ax3 = plt.subplot(313)
ax3.plot(t[:-4], d2zdt2_CD)
plt.grid(True)
plt.xlabel('t')
plt.ylabel("f''(t)")

plt.savefig( '119_midterm_plot#3.png')                    