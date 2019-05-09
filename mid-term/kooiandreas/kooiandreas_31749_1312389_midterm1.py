#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:22:28 2019

@author: andreaskooi
"""


# lin_LS function taken from opt_utils
# My fit for Beta is found out to be -1.0



# imports and file names
import numpy as np
import matplotlib.pyplot as plt
file_in = 'star_luminos.txt'


# functions
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
    dLS['r_p'] = 1./N*CovXY/(aX.std()*aY.std())
    return dLS['a'] , dLS['b']








# loading

T, L = np.genfromtxt(file_in).T



# computations, selecting 10<T<1000, and fitting

sel_t = np.logical_and( T >= 10, T <= 1000)
#print(sel_t)


a,b = lin_LS( np.log10( T[sel_t]), -np.log10( T[sel_t]))
print('a is %0.2f, and Beta is %0.2f'%(a,b))
print(b)




#plotting 

#I had a hard time getting the ranges to show on the plots so I just plotted the fit
# I obtained on a different subplot

plt.subplot(221)
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)


ax1.loglog( T[sel_t], L[sel_t], 'ko')
ax2.plot( np.log(T), b* np.log(T)) 


ax1.set_title('Log-Log graph of L and T')
ax1.set_xlabel('log(T), temperature')
ax1.set_ylabel('log(L), luminosity')


ax2.set_title('Linear fitting of the log transformation of L and T. L = T^ %0.2f'%b)
ax2.set_xlabel('log(T), temperature')
ax2.set_ylabel('b*log(L), luminosity. ')



plt.show()





