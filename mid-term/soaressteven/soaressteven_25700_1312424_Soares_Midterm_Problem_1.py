# -*- coding: utf-8 -*-
#python2.7


import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
#                     Functions from opt_utils.py
# =============================================================================

# Just to be sure of what code I am using, I will just copy and paste the
# functions from opt_utils.py into here, instead of importing it

# If I am supposed to import it, just know that I know how to do that:
# import opt_utils.py as opt
# Later on I would type opt.lin_LS( aX, aY)

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
    dLS['b'] = CovXY/VarX # eq. 1
    dLS['a'] = meanY - meanX*dLS['b'] # eq. 2
    dLS['Y_hat'] = dLS['b']*aX + dLS['a']
    # goodness-of-fit
    ResSS    = ( ( dLS['Y_hat'] - aY)**2).sum()
    dLS['R2']= 1 - ResSS/VarY # eq. 3
    # correlation coefficient
    dLS['r_p'] = 1./N*CovXY/(aX.std()*aY.std())
    return dLS

# =============================================================================
#                             Define variables
# =============================================================================

star_luminos = 'E:/ASTR_119/star_luminos.txt'
data = np.genfromtxt(star_luminos).T

# =============================================================================
#                                   Plots
# =============================================================================


