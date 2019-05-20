# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:46:52 2019

@author: Emily White
"""
"""
4.     Using the Secant method, find the root of the following functions:
    (a) f1(x) = -x**5 + (x**2)/3 + 0.5 with -10<x<10
ANS: see figure 5
    (b) f2(x) = cos**2(x) + 0.1 with -10<x<10
ANS: see figure 6
    (c) f3(x) = sin(x/3) + 0.1(x+5) with -3<x<3
ANS: see figure 7
                ANS vvv bottom of script
"""
#=============================================================================
#                           modules
#=============================================================================
import numpy as np
import matplotlib.pyplot as plt

#=============================================================================
#                          fnc dfns FUNCTION 1
#=============================================================================
#for f1(x) -> xa
def fct1(xa):
    return -xa**5 + (xa**2)/3 + 0.5

def dfdxa(xa):
    return (2*xa)/3 - 5*xa**4


def my_Secant1(fct1, xa0, xa1, tol = 1e-6, Na = 20):
# tol = tolerance
    xa0 = float(xa0)
    xa1 = float(xa1)
    ia = 0
    while abs(fct1(xa1)) > tol and ia < Na:
        #numerical approx of derivative
        dfdta = (fct1(xa1) - fct1(xa0))/(xa1-xa0)
        # basically Newton
        xa_next = xa1 - fct1(xa1)/dfdta
        
        xa0 = xa1
        xa1 = xa_next
        print(ia, 'fct1_value', abs(fct1(xa0)), xa_next)
        ia+= 1
    # check if soln converged
    if abs(fct1(xa1)) > tol:
        return np.nan
    else:
        return xa1

#for f2(x) -> xb
def fct2(xb):
    return (np.cos(xb))**2 + 0.1

def dfdxb(xb):
    return -2*(np.cos(xb))*(np.sin(xb))

def my_Secant2(fct2, xb0, xb1, tol = 1e-6, Nb = 20):
    xb0 = float(xb0)
    xb1 = float(xb1)
    ib = 0
    while abs(fct2(xb1)) > tol and ib < Nb:
        dfdtb = (fct2(xb1) - fct2(xb0))/(xb1-xb0)
        xb_next = xb1 - fct2(xb1)/dfdtb
        
        xb0 = xb1
        xb1 = xb_next
        print(ib, 'fct2_value', abs(fct2(xb0)), xb_next)
        ib += 1
    if abs(fct2(xb1)) > tol:
        return np.nan
    else:
        return xb1
    
#for f3(x) -> xc
def fct3(xc):
    return (np.sin(xc/3)) + 0.1*(xc+5)

def dfdxc(xc):
    return (np.cos(xc/3))/3 + 1/10

def my_Secant3(fct3, xc0, xc1, tol = 1e-6, Nc = 6):
    xc0 = float(xc0)
    xc1 = float(xc1)
    ic = 0
    while abs(fct3(xc1)) > tol and ic < Nc:
        dfdtc = (fct3(xc1) - fct2(xc0))/(xc1-xc0)
        xc_next = xc1 - fct3(xc1)/dfdtc
        
        xc0 = xc1
        xc1 = xc_next
        print(ic, 'fct3_value', abs(fct3(xc0)), xc_next)
        ic += 1
    if abs(fct3(xc1)) > tol:
        return np.nan
    else:
        return xc1

#=============================================================================
#                       parameters
#=============================================================================
# for function 1
xa0 = -9
#independent variable range
xamin, xamax = -10, 10

#for function 2
xb0 = -9
xbmin, xbmax = -10, 10

#for function 3
xc0 = -2
xcmin, xcmax = -3, 3

#=============================================================================
#                   find roots
#=============================================================================
xa_rootSec = my_Secant1(fct1, xa0, xa0+10)
xb_rootSec = my_Secant2(fct2, xb0, xb0+10)
xc_rootSec = my_Secant3(fct3, xc0, xc0+3)

#=============================================================================
#                   plots
#=============================================================================
a_xa = np.linspace(xamin, xamax, 1000)
a_xb = np.linspace(xbmin, xbmax, 1000)
a_xc = np.linspace(xbmin, xbmax, 1000)

#function 1 plot
plt.figure(5)
plt.plot(a_xa, fct1(a_xa), 'k-')
plt.plot([xa_rootSec], [fct1(xa_rootSec)], 'b*', ms = 10) #b* blue star, ms is size of star
plt.plot([xamin, xamax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('xa')
plt.ylabel('Fct values f1(xa)')
plt.show()

#function 2 plot
plt.figure(6)
plt.plot(a_xb, fct2(a_xb), 'k-')
plt.plot([xb_rootSec], [fct2(xb_rootSec)], 'b*', ms = 10) #b* blue star, ms is size of star
plt.plot([xbmin, xbmax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('xb')
plt.ylabel('Fct values f2(xb)')
plt.show()


#function 3 plot
plt.figure(7)
plt.plot(a_xc, fct3(a_xc), 'k-')
plt.plot([xc_rootSec], [fct3(xc_rootSec)], 'b*', ms = 10) #b* blue star, ms is size of star
plt.plot([xcmin, xcmax], [0,0], 'r--',)
plt.grid(True)
plt.xlabel('xc')
plt.ylabel('Fct values f3(xc)')
plt.show()

"""
        FROM CONSOLE
(0, 'fct1_value', 0.16666666666666674, 0.9999717880719968)
(1, 'fct1_value', 0.166544422672253, 0.9615360409067213)
(2, 'fct1_value', 0.013732908326468785, 0.9580818863258979)
(3, 'fct1_value', 0.0012858335916072772, 0.957725058068236)
(4, 'fct1_value', 1.1544699001109215e-05, 0.9577218253045717)
(0, 'fct2_value', 0.3919265817264287, 8.281743699038909)
(1, 'fct2_value', 0.2720885368651351, 24.814715270726705)
(2, 'fct2_value', 1.0022236391317119, 2.12064826477091)
(3, 'fct2_value', 0.3730699952675163, -11.33628002783568)
(4, 'fct2_value', 0.211657792321673, -28.982180906840572)
(5, 'fct2_value', 0.6772405750300573, -3.3143072180795734)
(6, 'fct2_value', 1.0704651179828288, -73.18930339782713)
(7, 'fct2_value', 0.4548461338939843, -124.81599570208581)
(8, 'fct2_value', 0.5378488949193538, 209.71937470203895)
(9, 'fct2_value', 0.6180611448555882, -2367.9830858452033)
(10, 'fct2_value', 0.6076229065609156, -152419.26732662754)
(11, 'fct2_value', 0.13469080734189628, -195153.79232599674)
(12, 'fct2_value', 0.23246870979972709, -93551.6957296618)
(13, 'fct2_value', 0.1480960478963218, 84786.50795441847)
(14, 'fct2_value', 0.22766430766897838, -425482.83548317535)
(15, 'fct2_value', 0.20893022486006016, -6116217.1912030345)
(16, 'fct2_value', 0.1992030179158525, -122656500.98683666)
(17, 'fct2_value', 0.9395664020163063, 25240244.702258542)
(18, 'fct2_value', 0.16424880462839342, 56571745.19922133)
(19, 'fct2_value', 0.6800242986855599, 15262722.38269353)
(0, 'fct3_value', 1.757272626635812, -3.8407062431145533)
(1, 'fct3_value', 0.8421539549343529, 6.510634913827165)
(2, 'fct3_value', 1.9767291053583835, -9.340506708498326)
(3, 'fct3_value', 0.4621373941943903, -4.493386015325038)
(4, 'fct3_value', 0.946675212496171, -6.743175528835447)
(5, 'fct3_value', 0.9538177196025556, -4.794171164917664)

"""

