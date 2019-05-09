#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
MIDTERM QUESTION 1

@author: scarletpasser
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       import data 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#import data
star_data = np.loadtxt('star_luminos.txt', skiprows = 1).T


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            variables 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

temp  = star_data[0]  #star temp(degree C)
lumos = star_data[1]  #star luminosity(solar units)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           data fit  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#select data within 10 < temp < 10
seltemp = np.logical_and(temp > 10,  temp < 1000)

#updated data set
sel_data =  star_data.T[seltemp].T

temp  = sel_data[0]
lumos = sel_data[1]

#fitting data using least squares fit 
fit_data = opt_utils.lin_LS(temp, lumos) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           plots 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#plot of the data 
plt.title('star temp and luminosity')
plt.loglog( temp, lumos, label = 'lumos vs temp')


#plot of the fitted data 
plt.loglog( temp, fit_data['Y_hat'], label = 'fitted lumos vs temp') 


plt.xlabel('temp (degree C)')
plt.ylabel('lumos (solar units)')
plt.legend()

plt.savefig('Midterm #1 graph')
plt.show()


"""
I understand that there is something wring with my graph, 
unfortunatly I ran out of time :(
"""
