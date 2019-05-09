# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#=============================
# definitions
#=============================
file_in = 'midterm_dydx.txt'

mData = np.loadtxt( file_in).T

t = mData[0]
zt = mData[1]

def U(t):
    return T0*np.exp(-t**2)


#=============================
# plots
#=============================
    
plt.figure(1)
plt.subplot(211)
plt.plot( , , 'b-')
plt.subplot(212)
plt.plot( , , 'r-')
plt.show()