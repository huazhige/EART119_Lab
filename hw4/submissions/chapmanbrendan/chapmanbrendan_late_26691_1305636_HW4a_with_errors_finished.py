#python2.7
"""

    - create  temperature profile that follows:

        T_i = f_Tm + A cos( 2pi/w * t - phi)

        with some Gaussian error
"""
import numpy as np
from matplotlib import pyplot as plt
import os
#=======================================================================================
#                       fct definitions
#=======================================================================================
def fct_T ( t, Tm, A):
    return Tm + A*np.cos( (2*np.pi)/w * t )
np.random.seed(123456)
#=======================================================================================
#                       params
#=======================================================================================
dir_out = "./"
file_out = 'Hw4_1_fixed.png'
N     = np.array(1000)
f_Tm  =  10 # mean T in C
f_dA  =  40  # in degree C
w     =  3600
## noise / error
f_sigma = 15.2



#=======================================================================================
#                       create synthetic data
#=======================================================================================
a_t = np.linspace( 0, 7*w, 15000) # convert to martian days

a_T = fct_T( a_t, f_Tm, f_dA)
# add some noise
a_T_noise = np.random.randn(N* int(f_sigma))

#=======================================================================================
#                       save to file
#=======================================================================================
fig_ax = plt.subplot()
plt.plot( a_t, a_T_noise, "ko", ms = 2)
plt.plot( a_t, a_T, "r-", lw = 1.5)

# save this figure as .png


os.chdir (dir_out)
plt.savefig("fig_ax", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format="PNG",
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()

