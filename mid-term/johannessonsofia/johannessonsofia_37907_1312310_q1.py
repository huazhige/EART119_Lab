# -*- coding: utf-8 -*-

#imports
import numpy as np
import matplotlib.pyplot as plt

#functions
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

#variables
data = np.genfromtxt('star_luminos.txt')

data = data.T

T = data[0,:]

#find correct indexes
istart = 0
iend = 0
for i in range(len(T)):
    if T[i] < 10:
        istart +=1
    if T[i] <= 1000:
        iend += 1

L = data[1,istart:iend]
T = data[0,istart:iend]

#for fit
x = np.log10(T) 
y = np.log10(L)

#use fitfunction from opt_utils

fit = lin_LS(x,y)
alfa = 10**fit['a']
beta = fit['b']

def myFunc(t):
    l = alfa*t**beta
    return l

tt = np.linspace(10, 1000, 1000)

im = plt.figure(1)
plt.plot(T, L, 'r-')
plt.plot(tt, myFunc(tt), 'b-')
plt.xlabel('Temperature')
plt.ylabel('Luminosity')
plt.title('red line is data and the blue line is the fit')
im.savefig('q1.png')

#with red dots you could not see the blue curve