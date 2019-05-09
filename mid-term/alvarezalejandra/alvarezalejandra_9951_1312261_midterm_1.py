
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
np.random.seed( 123456)
#===================================================================================
#                           function def
#===================================================================================
#using from opt_utils.py
def lin_LS( aX, aY):
    dLS   = {}
    N     = len(aX)
    if len( aX) != len( aY):
        error_str = ( len( aX), len( aY))
        raise (ValueError, error_str)
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

#===================================================================================
#                          load data
#===================================================================================
Data = np.genfromtxt( 'star_luminos.txt', skip_header = 1, usecols=(0,1)).T
temp = Data[0]
lum = Data[1]

#print( temp, lum)
#===================================================================================
#                            fit data
#===================================================================================
dLS = lin_LS( np.log10( lum), np.log10( temp)) #log fitting data
for tag, item in dLS.items():
    if isinstance( item, (int, float)): #assignning variables as int and floats
        print( tag, item)

# compute model fit y_hat
lum_yhat =  10**dLS['a'] * (lum**dLS['b'])

#===================================================================================
#                              plots
#===================================================================================
plt.figure(1)
ax1 = plt.subplot(111)
ax1.loglog( lum, temp, 'ko', ms = 5, mew = 1, mfc = 'none')
ax1.plot(  lum, lum_yhat, 'r--', label = 'y = %.2f x + %.1f, R2=%.2f'%( dLS['b'], 10**dLS['a'], dLS['R2']))
plt.title('Luminosity vs Temperature')
ax1.set_xlabel( 'Temperature[degrees C]')
ax1.set_ylabel( 'Luminosity [solar units]')
#ax1.legend( loc = 'lower right')
plt.show()