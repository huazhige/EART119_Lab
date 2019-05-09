# -*- coding: utf-8 -*-
"""
Midterm #3
"""
import numpy as np
import matplotlib.pyplot as plt


data_dir ='C:\Users\conma\OneDrive\ASTR 119\My programs\Midterm'
file_in  = 'midterm_dydx.txt'

#load data
mData   = np.genfromtxt( file_in, usecols=(0, 1), skip_header = 1)
t = mData[0]
z = mData[1]

#find derivatives
a_dzdx   = np.zeros(len(t))
a_d2zdx2 = np.zeros(len(t))
dt = t[1] - t[0]

for i in range( 0, len(t) -1):
    a_dzdx   = ( z[i+1] - z[i-1])/(2*dt)    
    a_d2zdx2 = ( z[i+1] - 2*z[i] + z[i-1])/(dt**2)

#plots
plt.plot(t, z, 'k-', label = 'Initial Data')
plt.plot(t, a_dzdx, 'r-', label = 'First derivative') 
plt.plot(t, a_dzdx, 'g-', label = 'Second derivative')
plt.xlabel('t')
plt.ylabel('z(t)')
plt.legend()
plt.show()
