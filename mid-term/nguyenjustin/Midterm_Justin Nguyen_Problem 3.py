# -*- coding: utf-8 -*-
"""
Midterm
Anaconda 2, Python 2.7
@author: jnguy126
"""
import numpy as np
import matplotlib.pyplot as plt
import os

file_in = 'midterm_dydx.txt'

t,z = np.genfromtxt(file_in).T

delta_t = t[1::] - t[0:-1]

#Formulas for the first and second derivative
dz_dt = (z[2::] - z[0:-2]) / (2*delta_t[1::])
d2z_dt2 = (z[2::] - 2*z[1:-1] + z[0:-2]) /(delta_t[1::])**2

plt.subplot(311)

ax1 = plt.subplot(311) #Original
ax2 = plt.subplot(312) #1st deriv
ax3 = plt.subplot(313) #2nd deriv

ax1.plot(t,z)
ax2.plot(t[2::],dz_dt, 'r')
ax3.plot(t[2::],d2z_dt2, 'g')

plt.xlabel( 'Time[s]')
plt.ylabel( "                                                 z ''(t)                   z ' (t)                 z  (t) " )

os.chdir( 'X:\Earth119\Midterm') #changed path to my folder
plt.savefig( 'Midterm prob 3')
plt.show()
