#python2.7
"""

    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
import numpy as np #set it to name np
import matplotlib.pyplot as plt #plt not plot
import os
import scipy
from scipy import special

#=======================================================================================
#                       fct definitions
#=======================================================================================
def fct_T( t, f_Tm, f_dA , phi): #no colon
    return f_Tm + f_dA*np.cos( (2*np.pi)/w * t - phi )
np.random.seed(123456)
#=======================================================================================
#                       params
#=======================================================================================
dir_out = 'data'
file_out= 'Hw4_1_fixed.png'
t     = 100
phi   = 20
N     = 1000 # changed to 1000 so they match in line 48
f_Tm  =  10 # mean T in C
A     =  40  # in degree C
w     =  3600

## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
a_t = np.linspace( 0, 7*w, N) # multiplied w and 7

a_T = fct_T(a_t,f_Tm,A,w)
# add some noise
a_T_noise = a_T + np.random.randn(  N)*f_sigma


#=======================================================================================
#                       save to file
#=======================================================================================
fig, ax = plt.subplots()
plt.plot( a_t, a_T_noise, 'ko', ms = 2)
plt.plot( a_t, a_T, 'r-', lw = 1.5)

# save this figure as .png
os.chdir( 'X:\EART119_test') #directed into a new folder
plt.savefig( 'dir_out')
plt.show()