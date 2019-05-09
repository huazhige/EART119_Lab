# -*- coding: utf-8 -*-
"""

Question 1 least squares


"""

import numpy as np
import matplotlib.pyplot as plt
import os

#========================================================
#                   Data
#========================================================

mFile = 'star_luminos.txt'

mData = np.loadtxt(mFile).T

temp = mData[0]
lum  = mData[1]

#========================================================
#                   Least squares
#========================================================

def lin_LS( aX, aY):
    """
    - linear least squares assuming normal distributed errors in Y, no errors in X

    :param aX: - independent variable
    :param aY: - measured dependent variable

    :return: { 'a' :  float( <intercept>),
               'b' :  float( <slope>),
               'R2 :  float(), #coefficient of variation = r_p**2 for lin. regre
               'r_p:  float(), # correlation coefficient (Pearson)

               'Y_hat' : np.array(), # modeled values of aY using a and b
            }

    example:   TODO:
    """
    dLS   = {}
    N     = len(aX)
    if len( aX) != len( aY):
        error_str = 'input variable need to have same dimensions %i, %i'%( len( aX), len( aY))
        raise ValueError, error_str
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
    dLS['r_p'] = 1.
    return dLS


a = 515.9896349043293

b = -0.24207087442733877

at = np.arange(10, 1001)

def L (T):
    return a*T**b



#========================================================
#                   Plots
#========================================================


plt.figure(1)
plt.title('Temperature Vs Luminosity')
plt.plot(temp, lum)
plt.plot(at,L(at))

plt.xlabel('Temp (deg)')
plt.ylabel('Lum (solar units)')


os.chdir( 'X:\ASTRO 119\Astro119\midterm')
plt.savefig( 'Q1plt')
plt.show()
