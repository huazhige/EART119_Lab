#!/usr/bin/env python
# coding: utf-8

# In[6]:


#python2.7
"""

    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
import numpy as np
import matplotlib.pyplot as plot
import os
#=======================================================================================
#                       fct definitions
#=======================================================================================
def fct_T( t, Tm, A, w):
    return Tm + A*np.cos( (2*np.pi)/w * t )
np.random.seed(123456)
#=======================================================================================
#                       params
#=======================================================================================
dir_out = 'data'
file_out = 'Hw4_1_fixed.png'
N     = 1000
f_Tm  =  10 # mean T in C
f_dA  =  40  # in degree C
w     =  3600
## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
a_t = np.linspace( 0, 7*w) # convert to martian days

a_T = fct_T( a_t, f_Tm, f_dA, w)
# add some noise
a_T_noise = a_T + np.random.randn(  N)*f_sigma

#=======================================================================================
#                       save to file
#=======================================================================================
fig, ax = plt.subplots()
plot( a_t, a_T_noise, 'ko', ms = 2)
plot( a_t, a_T, 'r-', lw = 1.5)

# save this figure as .png
os.chdir( data)
plt.savefig( 'dir_out')
plt.show()


# In[ ]:




