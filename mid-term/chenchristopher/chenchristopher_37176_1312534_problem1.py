# -*- coding: utf-8 -*-
#python2.7
"""
Midterm problem 1
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

#==============================================================================
#load data
#==============================================================================
data = np.loadtxt('star_luminos.txt').T
temp = data[0]
lum = data[1]

#==============================================================================
#computations
#==============================================================================
#we're only interested in temperatures between 10 and 1000 exclusive
sel = np.logical_and(temp > 10, temp < 1000)
temp = temp[sel]
lum = lum[sel]

#data can be described by l=alphaT^beta so it can be linearized by plotting logT vs logl
#take the log
lintemp = np.log10(temp)
linlum = np.log10(lum)

#fit the data
model = opt_utils.lin_LS(lintemp, linlum) #note model is a dictionary

#==============================================================================
#plotting
#==============================================================================
plt.figure()

#linearized data
plt.plot(lintemp, linlum, 'ko')

#predicted values using our least squares model
plt.plot(lintemp, model['Y_hat'], 'b-')

#labelling
plt.xlabel('Log of Temperature')
plt.ylabel('Log of Lumosity')
plt.title('Linear Model of Temperature vs. Luminosity')

#==============================================================================
#printing
#==============================================================================
print('The power law exponent is ' + str(model['b']) + '.')