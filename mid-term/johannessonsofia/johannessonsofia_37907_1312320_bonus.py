# -*- coding: utf-8 -*-

#imports
import numpy as np
import matplotlib.pyplot as plt

#================================
#           functions
#================================
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

#===================
#   varibales
#===================

Data = np.loadtxt('midterm_dydx.txt').T
t = Data[0,:]
z = Data[1,:]
N = len(t)
dt = t[1]-t[0] #assume its equidistand
dt = float(dt)

#=====================
#  calculations
#=====================
#exponential fit

fitx= t**2
fity = np.log(z)
fit = lin_LS(fitx, fity)

#just to check
print('b=' + str(fit['b']) + ' should be -1')
T0 = np.exp(fit['a'])

def myFunc(tt):
    return T0*np.exp(-tt**2)

myU = myFunc(t)


#derivative
dzdt = []
mydzdt = []
tt = []
for i in range(N-2):
    diff = z[i+2]-z[i]
    temp = diff/(2*dt)
    dzdt.append(temp)
    
    mydiff = myU[i+2]-myU[i]
    mytemp = mydiff/(2*dt)
    mydzdt.append(mytemp)
    
    tt.append(t[i+1])


#second derivative, note that the equation in the lecture notes is wrong
ddzdtt = []
myddzdtt = []
for i in range(N-2):
    diff = z[i+2]-2*z[i+1]+z[i]
    temp = diff/(dt**2)
    ddzdtt.append(temp)
    
    mydiff = myU[i+2]-2*myU[i+1]+myU[i]
    mytemp = mydiff/(dt**2)
    myddzdtt.append(mytemp)

#=====================    
#         plots
#=====================
im = plt.figure(1)
pIm1 = plt.subplot( 311)
plt.plot(t,z,'b-')
plt.plot(t, myU, 'r-')
plt.title('Position (blue-exact and red - nummerical)')
plt.xlabel('x')
plt.ylabel('y')

pIm2 = plt.subplot(312)
plt.plot(t[1:N-1],dzdt,'b-')
plt.plot(t[1:N-1],mydzdt,'r-')
plt.title('Velocity')
plt.xlabel('x')
plt.ylabel('dy/dt')

pIm3 = plt.subplot(313)
plt.plot(t[1:N-1],ddzdtt, 'b-')
plt.plot(t[1:N-1],myddzdtt, 'r-')
plt.title('Acceleration')
plt.xlabel('x')
plt.ylabel('d^2y/dt^2')
#the acceleration is mostly constant, ony small variances,
# probably due to the discretization

im.savefig('bonus.png')