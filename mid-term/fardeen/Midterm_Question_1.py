import numpy as np
import matplotlib.pyplot as plt
import os
import opt_utils as utils

# Importing data file
data_file = 'star_luminos.txt'
mData = np.loadtxt(data_file).T
aTemp, aLumi = mData[0], mData[1]


xmin, xmax = 10, 1000

dLS = utils.lin_LS(aTemp, aLumi)

a_yhat =  dLS['a'] + (dLS['b']*aTemp)



plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot(aTemp, aLumi, 'ko', ms = 2, mew = 1, mfc = 'none', label='scatterplot')
ax1.plot(  aTemp, a_yhat, 'r--', label = 'L = a * T^b ')
ax1.set_xlabel('Temperature [Degrees Celsius]')
ax1.set_ylabel('Luminosity [Solar Units]')
ax1.set_xlim(10, 1000)
ax1.set_ylim(0, 1000)
ax1.legend()
plt.show()
