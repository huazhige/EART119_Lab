# -*- coding: utf-8 -*-
"""
Benny Quiroz
1680808
Problem 1
"""

import numpy as np
import matplotlib.pyplot as plt
import os 

def lin_LS( aX, aY):
    """
    From opt_utils. Didn't want to worry about importing incositencies so I copy pasted.
    Took out the comments cuz you wrote it lol. 
    """
    dLS   = {}
    N     = len(aX)
    if len( aX) != len( aY):
        error_str = 'input variable need to have same dimensions %i, %i'%( len( aX), len( aY))
        print( error_str)
    meanX = aX.mean()
    meanY = aY.mean()
    # variance and co-variance - 1./N term omitted because it cancels in the following ratio
    VarX  = ( (aX - meanX)**2).sum()
    VarY  = ( (aY - meanY)**2).sum()
    CovXY = ( (aY-meanY)*(aX-meanX)).sum()

    # slope and intercept, and fit
    dLS['b'] = CovXY/VarX
    dLS['a'] = meanY - meanX*dLS['b']
    dLS['Y_hat'] = dLS['b']*aX + dLS['a']
    # goodness-of-fit
    ResSS    = ( ( dLS['Y_hat'] - aY)**2).sum()
    dLS['R2']= 1 - ResSS/VarY
    # correlation coefficient
    dLS['r_p'] = 1./N*CovXY/(aX.std()*aY.std())
    return dLS

path = 'C:\\Users\\benit\\Python Scripts\\119 Midterm'
os.chdir(path)
file_in = 'star_luminos.txt'

#Sel used to get only temps between 10 and 1000. Makes the logs work later. 
aStar = np.loadtxt(file_in, comments = '#').T
sel = np.logical_and(aStar[0] > 10, aStar[0] < 1000)
aStar = np.array([aStar[0][sel], aStar[1][sel]])
                   
#Pretty simple first plot, just the raw data.
plt.figure(1)
plt.tight_layout()
plt.subplot(211)
plt.plot(aStar[0], aStar[1])
plt.xlabel('Temperature in C')
plt.ylabel('Luminosity in SU')
plt.title('Luminosity v. Temp')

#Logging the data
logt =  np.log10(aStar[0])
logl =  np.log10(aStar[1])
plt.subplot(212)
#ploting the logs against each other
plt.plot(logt, logl, 'ko', ms = 1)
dDic = lin_LS(logt, logl)
plt.plot(logt, dDic['Y_hat'], 'r-')
#Getting the r-squared and the power-law exponent
legend = 'R-squared= %.3f    exp= %.3f'%(dDic['R2'], dDic['b'])
#Putting the text on there. 
plt.text(1, 1.1, legend)
plt.xlabel('Log of Temp in C')
plt.ylabel('Log of Lum in SU')
plt.title('Log(Lum) v. Log(Temp)')
plt.show()