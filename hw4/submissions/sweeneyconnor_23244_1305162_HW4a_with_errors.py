#python2.7
"""

    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
import numpy as np  #added as np
import matplotlib.pyplot as plt   #plt <-- plot
import os
#=======================================================================================
#                       fct definitions
#=======================================================================================
def fct_T( t, Tm, A):     #added comma b/w t, Tm; addeed colon
    return Tm + A*np.cos( (2*np.pi)/w * t )
np.random.seed(123456)
#=======================================================================================
#                       params
#=======================================================================================
dir_out = 'C:\Users\Connor\OneDrive\ASTR 119\Homework\HW4'
file_out = 'HW4_vertTraj.txt'
N     =  1000
f_Tm  =  10 # mean T in C
f_dA  =  40  # in degree C
w     =  3600
## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
a_t = np.linspace( 0, 7*w, N) # convert to martian days

a_T = fct_T( a_t, f_Tm, f_dA)

"""
print a_t

print a_t
print f_Tm
print f_dA
"""
# add some noise
noise =  np.random.randn(  N).dot( f_sigma)
a_T_noise = a_T + noise


#=======================================================================================
#                       save to file
#=======================================================================================
fig, ax = plt.subplots()
plt.plot( a_t, a_T_noise, 'ko', ms = 2) #added plt; a_T_noise --> a_T 
plt.plot( a_t, a_T, 'r-', lw = 1.5)     #added plt

# save this figure as .png
os.chdir( dir_out)   #dir_out <-- data
plt.savefig( 'dir_out')
plt.show() 