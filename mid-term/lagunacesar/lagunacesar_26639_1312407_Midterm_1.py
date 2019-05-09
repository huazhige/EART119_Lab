# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils
#=============== Data/ Data Import ===============#
file_eq = 'star_luminos.txt'
mData = np.loadtxt(file_eq).T

#=============== Power Law Fitting ===============#
x = np.log10(mData[0])
y = np.log10(mData[1])
#=============== Power Law Fitting ===============#
l_Ls = opt_utils.lin_LS(x, y)

T = np.arange(10, 1000)

ay_hat = (l_Ls['a']) * T* l_Ls['b']

plt.figure()
plt.plot(mData[0], mData[1], 'bo')

plt.loglog(mData[0], mData[1], 'g-')

#plt.loglog(mData[0], ay_hat, 'ro', mfc = 'none')
