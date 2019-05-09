#!/usr/bin/env python
# coding: utf-8

# In[47]:


#!python3
"""Error:invalid value encountered in power"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization

#data
star_lum = np.loadtxt('star_luminos.txt')
temp = star_lum[:,0]
lum = star_lum[:,1]

#initial guess
x0 = 0.4

#for graphing
leftlim = 10
rightlim = 1000
tempvec = np.linspace(0,1000, 100)
 
def func(a, temp, beta):
    lum =  a*temp**beta
    return lum


square = optimization.leastsq(func, x0, args=(temp, lum))
beta = square[0][0]
a = square[1]
print(a)
print(beta)

#plotting
plt.plot(temp, lum,label='data')
plt.xlim(leftlim, rightlim)
#best fit
plt.plot(func(a, tempvec, beta),label='Best fit')
plt.xlim(leftlim, rightlim)
plt.legend(loc='upper left')
plt.xlabel('Temperature: Degrees C')
plt.ylabel('Luminosity [Solar Units]')

plt.show()


# In[ ]:




