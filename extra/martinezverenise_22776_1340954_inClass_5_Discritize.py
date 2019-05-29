# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import fsolve
import integrate_utils as int_utils
 
"""
- We will be discretizing both fct_1 and fct_2 by solving for:
   - y'' + By = 0, y(0) = y0, y0(0) = 0, 
   - This wil be done for each function based on their given boundries 
-THEN, we will compute the mean value for each data set,  (Y, Y_2)

"""

########################### Functions Defenition ##############################
def fct_1(x):
    return np.sin(x)
def fct_1_dx(x):
    return np.cos(x)

def fct_2(x):
    return 2*x*np.exp(x**2)

def fct_2_dx(x):
    return 2*np.exp(x**2)*(2*x**2 + 1)

########################### Parameters ########################################
x1 = 0.0   #Params for first function 
x2 = np.pi

x3 = 0.0  #Params for second function 
x4 = 1
###############################################################################

###############################################################################

alpha = 0.0
B= 1.0 #Beta

N = 1000
X = np.linspace(x1, x2, N)
h = (x2 - x1) / (N - 1)

def Ypp(x, fct_1, fct_1_dx):
    return fct_1 *fct_1_dx

def residuals(fct_1):
    '''When we have the right values of y, this function will be zero.'''

    res = np.zeros(fct_1.shape)

    res[0] = fct_1[0] - alpha

    for i in range(1, N - 1):
        x = X[i]
        YPP = (fct_1[i - 1] - 2 * fct_1[i] + fct_1[i + 1]) / h**2
        YP = (fct_1[i + 1] - fct_1[i - 1]) / (2 * h)
        res[i] = YPP - Ypp(x, fct_1[i], YP)

    res[-1] = fct_1[-1] - B
    return res

# we need an initial guess
init = (B - alpha) / (x2 - x1) * X

Y = fsolve(residuals, init)
print(Y)



alpha = 0.0
B = 1.0 #Beta

N = 1000
X2 = np.linspace(x3, x4, N)
h = (x2 - x1) / (N - 1)

def Ypp_2(x, fct_2, fct_2_dx):
    '''define y'' = y*y' '''
    return fct_2 * fct_2_dx

def residuals(fct_2):
    '''When we have the right values of y, this function will be zero.'''

    res = np.zeros(fct_2.shape)

    res[0] = fct_2[0] - alpha

    for i in range(1, N - 1):
        x = X2[i]
        YPP = (fct_2[i - 1] - 2 * fct_2[i] + fct_2[i + 1]) / h**2
        YP = (fct_2[i + 1] - fct_2[i - 1]) / (2 * h)
        res[i] = YPP - Ypp_2(x, fct_2[i], YP)

    res[-1] = fct_2[-1] - B
    return res

# we need an initial guess
iniT = (B - alpha) / (x3 - x4) * X2

Y_2 = fsolve(residuals, iniT)
print(Y_2)
#############################     Mean Value   ################################
dataset_1 = Y 
x = np.mean(dataset_1)
print('Mean Value 1 ', x)

dataset_2 = Y_2
x_2 = np.mean(dataset_2)
print('Mean Value 2 ', x_2)

for n in np.arange(100, 1200, 200):
   fInt = int_utils.trapezoidal( fct_1,x1 - 1, x2 + 1, n)
   print('no. of random points', n, "num integral", round(fInt, 4), 'exact', round(2./3, 2))
for n in np.arange(100, 1200, 200):
   fInt = int_utils.trapezoidal( fct_2, x3 - 1, x4 + 1, n)
   print('no. of random points', n, "num integral", round(fInt, 4), 'exact', round(2./3, 2))




