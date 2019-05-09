"""
Lili Callahan
Midterm Problem 1

"""

import numpy as np
import matplotlib.pyplot as plt

############################################################################
#       Load Data
############################################################################

file_in = "star_luminos.txt"
data = np.genfromtxt(file_in, skip_header = 1).T

# specify columns to use
temp = data[0]
luminosity = data[1]

############################################################################
#       Log Transform Data
############################################################################

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
    return dLS

# select data of interest
sel_t = np.logical_and(temp > 10, temp < 1000)

# log transform
X, Y = np.log10(sel_t), np.log10(luminosity)

dPL = lin_LS(X, Y)
p_omori = dPL['b']
print p_omori

aOmori_rate = 10**(np.log10(sel_t)*p_omori + dPL['a'])

##############################################################################
#       Plotting
##############################################################################

plt.figure()
plt.loglog(temp, luminosity, 'ko', ms = 0.5, label = "Luminosity, p_omori = ")
plt.xlabel( 'Temperature (degree C)')
plt.ylabel( 'Luminosity (solar units)')
plt.loglog(temp, aOmori_rate)
plt.legend( loc = 'upper right')
plt.savefig("mt_1_plot")
plt.show()