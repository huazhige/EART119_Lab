#python2.7
"""
Jason Minera
    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
import numpy as np
import matplotlib.pyplot as plt
#import os
#=======================================================================================
#                       fct definitions
#=======================================================================================
def fct_T( t, Tm, A, w):
    return Tm + A*np.cos( (2*np.pi)/w * t )
np.random.seed(123456) #this has a random seed number of 123456
#=======================================================================================
#                       params
#=======================================================================================
#dir_out = 'data'
file_out= 'Hw4_1_fixed.png'
N     = 50
f_TM  =  10 # mean T in C
F_dA  =  40  # in degree C
w     =  3600
## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
a_t = np.linspace( 0, 7*w, N) # convert to martian days

a_T = ([fct_T( a_t, f_TM, F_dA, w)])
# add some noise
a_T_noise = a_T + np.random.randn(  N)*f_sigma

#=======================================================================================
#                       save to file
#=======================================================================================
fig,ax = plt.subplots()
plt.plot( a_t, a_T_noise, 'ko', ms = 2)
plt.plot( a_t, a_T, 'r-', lw = 1.5)
plt.xlabel('Time[days]')
plt.ylabel('Temperature[C]')
# save this figure as .png
#os.chdir( 'data')
plt.savefig(file_out)
plt.show()