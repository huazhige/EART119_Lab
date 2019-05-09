# -*- coding: utf-8 -*-
"""

Midterm: Problem 1
James Babbe
1395064

"""

import numpy as np
import matplotlib.pyplot as plt

#=====================================================
#               Import data
#=====================================================

data = np.genfromtxt('star_luminos.txt', comments = '#').T
T = data[0]    # get temp data
L = data[1]    # get luminsosity data                  

#=====================================================
#               Funct def
#=====================================================

# least-squares formula, from class example
def lin_LS( aX, aY):
    
    dLS   = {}
    N     = len(aX)
    if len( aX) != len( aY):
        error_str = 'input variable need to have same dimensions %i, %i'%( len( aX), len( aY))
        #raise ValueError, error_str
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

#=====================================================
#               Parameters
#=====================================================
sel = T > 10
T1 = T[sel]
sel2 = T1 < 1000
aY = T1[sel2]


L1 = L[sel]
aX = L1[sel2]

#=====================================================
#               Get fit
#=====================================================

aX_log = np.log10(aX)
aY_log = np.log10(aY) 
dLS = lin_LS( aX_log,aY_log)

model_Y = abs(np.log10(dLS['a']* aY**dLS['b']))

#=====================================================
#               Plot
#=====================================================

plt.figure()
plt.plot( aX_log, aY_log, 'ko', ms = 2, mew = 1.5, mfc = 'none', label = 'Obs.')
plt.plot( aX_log, model_Y, 'r-', label = 'Model')
plt.legend( loc='upper right')
plt.xlabel('Log T')
plt.ylabel('Log L')
plt.title('Log-Luminosity vs Log-Temperature(C)')
plt.savefig( '119_midterm_plot#1.png')
