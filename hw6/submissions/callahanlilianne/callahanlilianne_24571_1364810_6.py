"""

Solve 1D-Heat equation for change in planetary temperature with depth from surface.
Surface is headed by periodic boundary condition of the form cos(t)*fUin
    
PDE:
    du/dt = alpha*d^2u/dx^2 + g(x,t)
    g(x,t) =  0
    
Plot numerical and analytical solutions for each time step.

"""

import numpy as np
import matplotlib.pyplot as plt

##########################################################################
#       Function Definitions
##########################################################################

def fct_BC_L( t, fAmp, w):
    # boundary conditions
    return fAmp*np.cos(w*t)

def fct_u_exact( t, x, fAlpha, fAmp, w):
    # exact solution
    return fAmp * (np.exp(-x*np.sqrt(w/(2*fAlpha))))*np.cos(-x*(np.sqrt(w/(2*fAlpha))) + w*t)

##########################################################################
#       Parameters and Variables
##########################################################################
    
f_Alpha = 1e-5                  # m2/s
f_L     = 4.                    # max. depth in m
f_W     = (2*np.pi)/(1*24*3600) # frequency of temperature oscillation in 1/s

# boundary conditions
f_Uin   = 50.  # amplitude of temperature oscillation
f_Uout  = 0.   # in degree C

# initial conditions
f_U0    = 0

# spatial steps
i_Nx     = 60           # number of nodes in x
f_dx     = f_L/(i_Nx-1) # node spacing

# time
f_dt     = 0.001*(24*3600) # in days
f_tmax   = 10*(24*3600)    # 10 days

# plotting
plot_step = 40 # plot every nth step
print( 'delta t: ', f_dt, 'in [s],   stability lim for delta t: ', f_dx**2/(2*f_Alpha))

##########################################################################
#       Numerical Solution, Problem 1
##########################################################################

a_x    = np.linspace( 0, f_L, i_Nx)
a_t    = np.arange( 0, f_tmax+f_dt, f_dt)
i_Nt   = int(f_tmax/f_dt)+1 # nodes in t
print('space', i_Nx, len( a_x), a_x[1]-a_x[0],    f_dx)
print('time',  i_Nt, len( a_t), round(a_t[1]-a_t[0],2), f_dt)

# initial conditions
a_U     = np.ones(i_Nx)*f_U0
a_U[0]  = fct_BC_L( 0, f_Uin, f_W)

# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))

fig, ax1 = plt.subplots( )
for n in range( len(a_t)): # loop over time increments
    # set boundary conditions
    a_U[0]  = fct_BC_L( a_t[n], f_Uin, f_W)
    a_U[-1] = fct_BC_L( a_t[n-1], f_Uout, f_W)
    # solve spatial derivatives
    for i in range( 1, i_Nx-1): # spatial loop without boundary nodes
        # central difference solution
        a_dUdt[i] = f_Alpha*(((a_U[i+1] - 2*a_U[i] + a_U[i-1])/(f_dx**2)))
    # forward difference formula to get u(x,t)
    a_Unew = a_U + f_dt*a_dUdt
    # update the temperature profile for the next time step, otherwise only BC and IC are shown
    a_U    = a_Unew
    # exact solutions
    a_Uana = fct_u_exact(a_t[n], a_x, f_Alpha, f_Uin, f_W)
    
##########################################################################
#       Plotting, Problem 2
##########################################################################
    
    print 'time step: ', a_t[n]/(24*3600), 'd'
    if (n+1)%plot_step == 0:
        ax1.cla()
        ax1.set_title( 'Time Step: %.2f [d]'%( a_t[n]/(24*3600)))
        ax1.plot( a_U, -a_x, 'ko-', ms = 3, mew =1.5, mfc = 'w', label = 'u(x,t)-num')
        ax1.plot(  [0,0], [-a_x.max(), 0], '--', color = ' .5')
        # plot exact solution for comparison
        ax1.plot( a_Uana, -a_x, 'r--', lw = 1.5, label = 'u(x,t)-exact')
        ax1.set_xlabel( 'Temperature [degree C]')
        ax1.set_ylabel( 'Depth [m]')
        ax1.legend( loc = 'lower left')
        ax1.set_xlim( -f_Uin-1, f_Uin+1)
        plt.pause( 0.2)
        plt.savefig('6_plot.png')

##########################################################################
#       Short Answers, Problem 3
##########################################################################
    
"""
At what depth is the temperature variation less than 1 degree?
    The temp. variation is less than 1 degree at -2 meters below the surface.

How far would you have to dig if the surface temperature vary by +/-80 degrees?
    You would have to dig -2.5 meters below the surface.
    
"""





