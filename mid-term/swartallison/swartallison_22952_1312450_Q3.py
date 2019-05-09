# Allison Swart
# Astro/Earth 119 Midterm
# May 8, 2019

# anaconda2/python2.7

import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               Problem 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load file

file_in = np.genfromtxt( 'midterm_dydx.txt')
#print file_in

# Central difference formula

ind_var = file_in[0]
dep_var = file_in[1]

delta_t = 0.1
a_t = np.all( -range_in, range_in+delta_t, delta_t)
der_in = file_in( a_t)

dfdt_CD = (file_in( a_t + delta_t) - file_in( a_t - delta_t)) / delta_t
dfdt_CD = (der_in[2::] - der_in[0:-2]) / (2 * delta_t)


# PLOTS

plt.figure(1)
ax = plt.subplot()
ax.plot( ind_var, dep_var, 'k')
ax.xlabel( 'Time [sec]')
ax.ylabel( 'Position [m]')
ax.grid( True)