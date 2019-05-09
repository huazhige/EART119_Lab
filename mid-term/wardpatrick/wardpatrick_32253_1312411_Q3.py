# -*- coding: utf-8 -*-
"""

Q3 derivitives

"""


import numpy as np
import matplotlib.pyplot as plt
import os

#========================================================
#                   Data
#========================================================
mFile = 'midterm_dydx.txt'

mData = np.loadtxt(mFile).T

t = mData[0]
z  = mData[1]
dt    = t[1]-t[0]

#========================================================
#                   Derivitives
#========================================================

dzdt = (z[2::] - z[0:-2])/(2*dt)
d2zdt2 = (z[2::] - 2*z[1:-1] + z[0:-2])/(dt**2)
# add zeros at beginning and end for plotting purposes
dzdt = np.hstack( (0,dzdt, 0))
d2zdt2 = np.hstack( (0,d2zdt2, 0))


#========================================================
#                   Plots
#========================================================

plt.figure(1)

plt.subplot(311)
plt.ylabel('function')

plt.plot(t, z)
plt.subplot(312)
plt.ylabel('1st derrivitive')
plt.plot(t, dzdt)

plt.subplot(313)
plt.ylabel('2nd derrivitive')
plt.plot(t, d2zdt2)


os.chdir( 'X:\ASTRO 119\Astro119\midterm')
plt.savefig( 'Q3plt')
plt.show()