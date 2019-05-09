# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:23:55 2019
Problem 1
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as op

#files
file_in = 'star_luminos.txt'
temperature = np.genfromtxt(file_in, skip_header = 1, usecols = 0).T #in Celcius
luminosity = np.genfromtxt(file_in, skip_header = 1, usecols = 1).T

#linear least squares function
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

#data log transform
logtemperature = np.log(temperature)
logluminosity = np.log(luminosity)

dictionary_output = lin_LS(logtemperature, logluminosity)
a_yhat = 10**(dictionary_output['a'])


plt.figure(1)


#plotting
plot1 = plt.subplot(211)
plot1.set_title('Luminosity and Temperature of Stars')
plot1 = plt.plot(temperature, luminosity, 'k--', label = 'data')
plt.xlabel('Temperature')
plt.ylabel('Luminosity')
plt.xlim(10, 1000)
plt.legend(loc = 'upper right')
plot2 = plt.subplot(212)
plot2 = plt.plot(temperature, a_yhat, 'r--', label = 'power law fit')
plt.legend(loc = 'upper right')
plt.xlabel('Temperature')
plt.ylabel('Luminosity')

plt.show()
