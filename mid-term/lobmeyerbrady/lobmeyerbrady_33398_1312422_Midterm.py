# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:58:54 2019

@author: Brady
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt
Star_lums = 'star_luminos.txt'
data = np.genfromtxt(Star_lums, dtype=float, delimiter=('   '), skip_header=(1), usecols=(0, 1)).T
#print data
aX= data[0]>10 
aY= data[1]<592
#print aX
#print aY
pow_law_fit=opt.lin_LS(aX, aY)
print pow_law_fit
a = pow_law_fit['a']
b = pow_law_fit['b']
T = aX
L = a*T**b
print L

#plt.plot(aY, aX)
plt.plot(aX, L, set(label('star_luminosity')))
#('Star_Luminosity')
#plt.set_xlabel('Temp')
#plt.set_ylabel('Luminosity')
plt.show()