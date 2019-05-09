# -*- coding: utf-8 -*-


#=====================================
# import
#=====================================
import numpy as np
import matplotlib.pyplot as plt
import opt_utils

#=====================================
# definitions
#=====================================

file_star = 'star_luminos.txt'

mData = np.loadtxt(file_star).T


dDic = opt_utils.lin_LS( mData[0], mData[1])

a_y = dDic['a']*mData[0]**dDic['b']

#===================================
# parameters
#===================================

Tmin, Tmax = 10, 1000

#===================================
# plot
#===================================
mData[0] = np.linspace( Tmin, Tmax, 9981)
plt.figure( 1)
plt.plot( mData[0], mData[1], 'ko')
plt.xlabel( 'Temperature')
plt.ylabel( 'Luminosity')
plt.show()
