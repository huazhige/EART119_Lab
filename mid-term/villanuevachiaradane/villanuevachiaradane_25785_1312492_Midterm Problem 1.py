#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# =========================1=============================
#                    Import File
# =======================================================
# Importing the data file and transposing it
data_file = "star_luminos.txt"
lumi_data = np.genfromtxt(data_file, skip_header = 1, usecols = (0, 1), dtype = float).T

# =========================2=============================
#                 Function Definitions
# =======================================================
# lin_LS taken from opt_utils
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
    #if len( aX) != len( aY):
    #    error_str = 'input variable need to have same dimensions %i, %i'%( len( aX), len( aY))
    #    raise ValueError, error_str
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

# =========================3=============================
#                 Power-Law Fitting
# =======================================================
# Dictionary of fitted data
dDic = lin_LS(np.log10(lumi_data[0]), np.log10(lumi_data[1]))
print(dDic)

# Power-law fit
a_yhat = 10**(dDic['a'])*lumi_data[0]**dDic['b']

# =========================4=============================
#                      Plotting
# =======================================================
plt.figure(1)

# Plotting the original data
plt.subplot(211)
plt.title("Luminosity Data")
plt.plot(lumi_data[0], lumi_data[1], 'ko')

# Plotting with double-log scales
plt.subplot(212)
plt.loglog(lumi_data[0], lumi_data[1], 'ko')
plt.loglog(lumi_data[0], a_yhat, 'r--')

# Grid formatting
plt.ylim(10, 1000)
plt.xlabel('Temperature [C]')
plt.ylabel('Luminosity [Solar Units]')

# Show the plots
plt.savefig('Problem 1')
plt.show()


# In[ ]:




