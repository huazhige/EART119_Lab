# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:27:25 2019

@author: Brady
"""

import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as inte
from mpl_toolkits.mplot3d import axes3d
e= np.e
pi= np.pi
sin = np.sin
cos = np.cos
sqrt = np.sqrt
intan= np.arctan

def fct_xy( x, y):
    return x*y**2

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct_Fct_exact(x,y):
    return 0.5*(x**2)*(1./3(y**3))

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)

#================================================
#          compute integral 
#================================================
for n in np.arange(100, 10000, 1000):
    f_MC1=inte.monteCarlo(fct_xy, fct_gxy, xmin-1, xmax+1, ymin-1, ymax+1, n)
    print('n', n, 'numerical sol:', f_MC1)

#================================================
#            plotting
#================================================
m_X, m_Y = np.meshgrid( a_x, a_y)
m_Z      = fct_xy( m_X, m_Y)
#m_Z      = fct2_xy( m_X, m_Y)
#
fig1 = plt.figure(1, figsize=(10,10))    
ax = axes3d.Axes3D( fig1)
plot1 = ax.plot_surface( m_X, m_Y, m_Z, cmap = plt.cm.coolwarm_r, linewidth=0, shade = True)
cbar = plt.colorbar( plot1, shrink = .5, aspect = 20)
##-----------------labels and legends-------------------------------------
cbar.set_label( 'f(x,y)')
ax.set_xlabel( 'x')
ax.set_ylabel( 'y')
ax.set_zlabel( 'z = f(x,y)')
plt.show()

# =============================================================================
# part a
# =============================================================================

xmin_fx, ymin_fx= -2, -2
xmax_fx, ymax_fx= 2, 2
xmin_gx=0
xmax_gx=2
ymin_gx, ymax_gx= 0, 1.5
N=1000


x= np.linspace(xmin_fx, xmax_fx, N, float)
y= np.linspace(ymin_fx, ymax_fx, N, float)

def fct2_xy( x, y):
    return sqrt(x**2 + y**2)
a= intan(y/x)
x= fct2_xy(x,y)
print a
print x

#Ifxy=inte.monteCarlo(x, fy, xmin_fx, xmax_fx, ymin_fx, ymax_fx, N)
#print Ifxy


