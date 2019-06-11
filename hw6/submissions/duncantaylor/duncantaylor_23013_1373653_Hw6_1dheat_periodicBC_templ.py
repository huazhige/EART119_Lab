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
#=========================0===========================================
#               function definitions
#=====================================================================
def fct_BC_L( t, fAmp, w):
    """
    set boundary condition as cos function with amplitude fAmp
    :param curr_t:
    :param fAmp:
    :return:
    """

    return fAmp*np.cos(t*w)

def fct_u_exact( t, x, fAlpha, fAmp, w):
    """
    exact solution to the 1D heat equation with periodic boundary condition of the form
    u_BC(t) = fAmp*sin(2pi/w * t)
    :param t:
    :param fAmp:
    :param w:
    :return:
    """
    # TODO return exact solution
    #return ???????
    return fAmp *np.e **(-x *(w /(2*fAlpha))**(1/2))*np.cos(-x *(w/(2*fAlpha))**(1/2)+ w *t)
#=====================================================================
#                   params
#=====================================================================
f_Alpha = 10**(-5) #m2/s
f_L     = 4    # max. depth in m
# boundary condition
f_Uin   = 50 # amplitude of temperature oscillation
f_Uout  = 0.   # in degree C
# frequency of temperature oscillation in 1/s
f_W     = (2*np.pi)/(1*24*3600)
# initial conditions
f_U0    = 0

# spatial steps
i_Nx     = 60 # number of nodes in x
f_dx     = f_L/(i_Nx-1) # node spacing
# time
f_dt     = 0.001*(24*3600)#in days
f_tmax   = 10*(24*3600) # 10 days
print f_dt

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
a_U     = np.zeros(len(a_x))
# make sure that IC and BC match
a_U[0]  = fct_BC_L( 0, f_Uin, f_W)

# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))

print('len a_U: ' + str(len(a_U)))

#plt.figure(1)
fig, ax1 = plt.subplots( )
for n in range( len(a_t)):# loop over time increments
    ##A##----set BC-----
    a_U[0]  = fct_BC_L( a_t[n], f_Uin, f_W)
    a_U[-1] = fct_BC_L( a_t[n], f_Uout, f_W)
    ##B##-----solve spatial derivatives---------------
    for i in range( 1, i_Nx-1): #spatial loop without boundary nodes
        # TODO: central difference solution
        a_dUdt[i] = f_Alpha*((a_U[i+1]-2*a_U[i]+a_U[i-1])/f_dx**2)

    # solve RHS in vectorized form:
    #a_dUdt[1:-1] = f_Alpha*(( a_U[2::] + a_U[0:-2] - 2*a_U[1:-1])/f_dx**2)

    ##C## integration step: forward difference Formula to get u(x,t)
    a_Unew = a_U + f_dt*a_dUdt
    # update the temperature profile for the next time step, otherwise only BC and IC are shown
    a_U    = a_Unew
    r_diff = 1
    ##D##---TODO: computer exact solution
    a_Uana = fct_u_exact(a_t[n], a_x, f_Alpha, f_Uin, f_W)
    #=========================3===========================================
    #               plot temp. u(x) for every mth time step
    #=====================================================================
    print 'time step: ', a_t[n]/(24*3600), 'd'#,(n+1)/plot_step,(n+1)%plot_step
    if (n+1)%plot_step == 0:
        ax1.cla()
        ax1.set_title( 'Time Step: %.2f [d]'%( a_t[n]/(24*3600)))
        ax1.plot( a_U, -a_x, 'ko-', ms = 3, mew =1.5, mfc = 'w', label = 'u(x,t)-num')
        ax1.plot(  [-f_Uin, f_Uin], [-2*r_diff, -2*r_diff], 'r--', label = '2 x l_diff')
        ax1.plot(  [0,0], [-a_x.max(), 0], '--', color = ' .5')
        # plot exact solution for comparison
        ax1.plot( a_Uana, -a_x, 'r--', lw = 1.5, label = 'u(x,t)-exact')
        ax1.set_xlabel( 'Temperature [degree C]')
        ax1.set_ylabel( 'Depth [m]')
        ax1.legend( loc = 'lower left')
        ax1.set_xlim( -f_Uin-1, f_Uin+1)
        plt.pause( 0.2)

        #plt.show()







