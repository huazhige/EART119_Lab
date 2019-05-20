#python3.7
"""

    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
"""
That above description is so terribly written, I'm not quite sure what this script
is supposed to do. I fixed the code so that it makes a pretty plot but what this has to 
Mars I have little idea. 
"""
#Import numpy as np and matplotlib.plyplpot as plt for future function calls
import numpy as np
import matplotlib.pyplot as plt
import os
#=======================================================================================
#                       fct definitions
#=======================================================================================
#Added in a comma 
def fct_T( t, Tm, A):
    return Tm + A*np.cos( (2*np.pi)/w * t )
np.random.seed(123456)
#=======================================================================================
#                       params
#=======================================================================================
dir_out = 'data'
file_out= 'Hw4_1_fixed.png'
N     = 1000
f_Tm  =  10 # mean T in C
f_dA  =  40  # in degree C
w     =  3600
## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
#Creating an array of length 1000,
a_t = np.linspace( 0, 7*w, 1000) # convert to martian days

a_T = fct_T( a_t, f_Tm, f_dA)
# add some noise
#They will now both be length 1000,
a_T_noise = a_T + np.random.randn(  N)*f_sigma

#=======================================================================================
#                       save to file
#=======================================================================================
fig, ax = plt.subplots()
plt.plot( a_t, a_T_noise, 'ko', ms = 2)
plt.plot( a_t, a_T, 'r-', lw = 1.5)

#You need to put the path that you want to save the file to in the os.chdir() function
path = 'C:\\Users\\benit\\Python Scripts\\HW4'
os.chdir( path)
#save this figure as .png
plt.savefig( file_out)
plt.show()