# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:23:30 2019

@author: emlowhit

            Best fitting model using least-squares


"""

#=============================================================================
#                      IMPORTS
#=============================================================================

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123456)
# prof fnc
import opt_utils as utils

#=============================================================================
#                       FILES
#=============================================================================
file_star = 'star_luminos.txt'


#=============================================================================
#                       LOAD DATA
#=============================================================================
sData = np.genfromtxt(file_star, skip_header = 1, usecols = (0,1)).T
s_temp, s_lumi = sData[0], sData[1] 


print(s_temp, s_lumi)
#=============================================================================
#                       FIT DATA
#=============================================================================
sLS = utils.lin_LS(np.log10(abs(s_temp)), np.log10(s_lumi))
for tag, item in sLS.items():
   if isinstance(item, (int, float)):
      print(tag,item)

s_yhat = 10**sLS['a']*(s_temp**sLS['b'])

#=============================================================================
#                       PLOTS
#=============================================================================
plt.figure(1)
ax1 = plt.subplot(111)
ax1.loglog(s_temp, s_lumi, 'ko', ms = 1, mew =1 , mfc = 'none', label = 'obs.')
ax1.plot(s_temp, s_yhat, 'r--', label = 'y = %.2f x + %.1f, R2=%.2f'%(sLS['b'], 10**sLS['a'], sLS['R2']))
ax1.set_xlabel('Temperature [degrees C]')
ax1.set_ylabel('Luminosity [solar units]')
ax1.legend(loc = 'lower left')
plt.show()










