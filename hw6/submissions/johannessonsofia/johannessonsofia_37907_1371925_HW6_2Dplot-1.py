# -*- coding: utf-8 -*-

#! python2.7
"""
Solve 1D-Heat equation for change in planetary temperature with depth from surface
      - surface is headed by periodic boundary condition of the form cos(t)*fUin
    PDE:
        du/dt     = alpha*d^2u/dx^2 + g(x,t)
                    g(x,t) =  0

         - plot numerical and analytical solutions for each time step
        --> create animation

"""
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#=========================0===========================================
#               function definitions
#=====================================================================
def fct_BC_L( t, fAmp, w):
    """
    set boundary condition as cos function with amplitude fAmp
    :param curr_t:
    :param fAmp:
    :return: fAmp*cos(w*t)
    """

    return fAmp*np.sin(w*t) #changed to sin just to start at 0, same period though

def fct_u_exact( t, x, fAlpha, fAmp, w):
    """
    exact solution to the 1D heat equation with periodic boundary condition of the form
    u_BC(t) = fAmp*sin(w * t)
    :param t: time
    :param fAmp: amplitude of BC
    :param w: angular frequency of BC
    :return: temperature at depth x at time t
    """
    # return exact solution
    return fAmp*np.exp(-x*np.sqrt(w/(2*fAlpha)))*np.sin(-x*np.sqrt(w/(2*fAlpha))+w*t)

#=====================================================================
#                   params
#=====================================================================
f_Alpha = 1e-5 #m2/s
f_L     = 4    # max. depth in m
# boundary condition
f_Uin   = 80 # amplitude of temperature oscillation (default 50)
f_Uout  = 0.   # in degree C (the average temperature)
# frequency of temperature oscillation in 1/s
f_W     = (2*np.pi)/(1*24*3600)
# initial conditions
f_U0    = f_Uout #begin at max

# spatial steps
i_Nx     = 60 # number of nodes in x
f_dx     = f_L/(i_Nx-1) # node spacing
# time
f_dt     = 0.001*(24*3600)#in days #change this one
f_tmax   = 10*(24*3600) # 10 days
plotStep = 100


#########plotting
plot_step = 40 #plot every nth step
print( 'delta t: ', f_dt, 'in [s],   stability lim for delta t: ', f_dx**2/(2*f_Alpha))


#=============================2=======================================
#                     solve 1d-heat
#=====================================================================
#a_x    = np.linspace( .5*dx, fL-.5*dx, iNx)#np.arange( .5*dx, fL-.5*dx, dx)
a_x    = np.linspace( 0, f_L, i_Nx)
a_t    = np.arange( 0, f_tmax+f_dt, f_dt)
i_Nt   = int(f_tmax/f_dt)+1 # nodes in t
print('space', i_Nx, len( a_x), a_x[1]-a_x[0],    f_dx)
print('time',  i_Nt, len( a_t), round(a_t[1]-a_t[0],2), f_dt)

# IC: aU0 = const ( = 0)
a_U = np.zeros((int(len(a_t)/plotStep), len(a_x)))

a_U[0,:]    = f_U0*np.ones(len(a_x))
a_Utemp = a_U[0,:]
# make sure that IC and BC match
a_U[0,0]  = fct_BC_L( 0, f_Uin, f_W)

# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))

#calculate where the temperature varies +/- 1 degree 
depthIdx = 0
idx = 1
counter = 0

#plt.figure(1)
fig, ax1 = plt.subplots( )
for n in range( len(a_t)-1):# loop over time increments
    ##A##----set BC-----
    a_Utemp[0]  = fct_BC_L( a_t[n], f_Uin, f_W)
#    a_U[-1] = f_Uout
    ##B##-----solve spatial derivatives---------------
    for i in range( 1, i_Nx-1): #spatial loop without boundary nodes
        # central difference solution
        a_dUdt[i] = f_Alpha*(a_Utemp[i+1]-2*a_Utemp[i]+a_Utemp[i-1])/f_dx**2


    ##C## integration step: forward difference Formula to get u(x,t)
    a_Unew = a_Utemp +  f_dt*a_dUdt
    
    while (np.abs(a_Unew[depthIdx])>1):
        depthIdx += 1
    depth = depthIdx*f_dx
    # update the temperature profile for the next time step, otherwise only BC and IC are shown
    a_Utemp    = a_Unew
    #put every 100th solution in matrix
    counter += 1
    if counter == plotStep:
        idx += 1
        if idx < 100:
            a_U[idx, :] = a_Utemp
        counter = 0
        
    #=========================3===========================================
    #               plot temp. u(x) for every mth time step
    #=====================================================================
    print 'time step: ', a_t[n]/(24*3600), 'd'#,(n+1)/plot_step,(n+1)%plot_step

fig2, ax2 = plt.subplots( )
ax2.cla()
ax2.set_title( 'Time Step: %.2f [d]'%( a_t[n]/(24*3600)))

ax2.imshow(a_U,
               origin='lower', extent=[0, -4, 0, 5],
               vmax=abs(a_U).max(), vmin=-abs(a_U).max())
       
 
ax2.set_xlabel( 'Depth [m]')
ax2.set_ylabel( 'Time elapsed [2 days]')






