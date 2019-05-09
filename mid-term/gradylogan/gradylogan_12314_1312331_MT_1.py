# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                           function def
#===================================================================================
import opt_utils as utils

#===================================================================================
#                           files, parameters
#===================================================================================
star_file = 'star_luminos.txt'

#===================================================================================
#                          load data
#===================================================================================
mData = np.genfromtxt( star_file, skip_header = 1, usecols=(0,1)).T
temp, sol = mData[0], mData[1]

print( temp, sol) 
#===================================================================================
#                            fit data
#===================================================================================
dLS = utils.lin_LS( np.log10( sol), np.log10( temp))
for tag, item in dLS.items():
    if isinstance( item, (int, float)):
        print( tag, item)

# compute model fit y_hat
a_yhat =  10**dLS['a'] * (sol**dLS['b'])

#===================================================================================
#                              plots
#===================================================================================
plt.figure(1)
ax1 = plt.subplot(111)
ax1.loglog( sol, temp, 'ko', ms = 5, mew = 1, mfc = 'none')
# ax1.hexbin( a_x, a_y, cmap = plt.cm.Blues)
ax1.set_xlabel( 'Luminosity(Solar Units)')
ax1.set_ylabel( 'Temperature (Degree C)')

plt.savefig('Midterm_Prob1_Plot')