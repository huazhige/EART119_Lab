#! python2.7
"""
Solve 1D-Heat equation for change in planetary temperature with depth from surface
      - surface is headed by periodic boundary condition of the form cos(t)*fUin
    PDE:
        du/dt     = alpha*d^2u/dx^2 + g(x,t)
                    g(x,t) =  0

         - plot numerical and analytical solutions for each time step
        --> create animation

@author: scarletpasser
"""
import numpy as np
import matplotlib.pyplot as plt

#=====================================================================
#                        Function definitions
#=====================================================================
def fct_BC_L( t, fAmp, w):
    """
    set boundary condition as cos function with amplitude fAmp
    :param curr_t: time vector 
    :param fAmp:   amplitude of cos function (change in temp b/n day and night)
    :return:       Boundary condition: fAmp * cos(wt)
    """
    return fAmp * np.cos(w*t)

def fct_u_exact( t, x, fAlpha, fAmp, w):
    """
    exact solution to the 1D heat equation with periodic boundary condition of the form
    u_BC(t) = fAmp*sin(2pi/w * t)
    :param t:    time vector
    :param fAmp: amplitude of the cos function (change in temp b/n day and night)
    :param w:    frequency (2pi/period) in (1/sec)
    :return:     exact solution: fAmp * e^-x*sqrt(w/2alpha) * cos(-x*sqrt(w/2alpha)+wt)
    """
    return fAmp * np.exp(-x*np.sqrt(w/(2*fAlpha)))*np.cos(-x*np.sqrt(w/(2*fAlpha)) + w*t)

#=====================================================================
#                              Params
#=====================================================================
f_Alpha = 1e-5 # m2/s
f_L     =  4   # max. depth in m
# boundary condition
f_Uin   = 50  # amplitude of temperature oscillation
f_Uout  = 0.   # in degree C
# frequency of temperature oscillation in 1/s
f_W     = (2*np.pi)/(1*24*3600)
# initial conditions - constant initial temp
f_U0    = 0
# spatial steps
i_Nx     = 60 # number of nodes in x
f_dx     = float(f_L)/(i_Nx - 1) # node spacing
# time
f_dt     = 0.001*(24*3600)#in days
f_tmax   = 10*(24*3600) # 10 days

#########plotting############
plot_step = 40 #plot every nth step
print( 'delta t: ', f_dt, 'in [s],   stability lim for delta t: ', f_dx**2/(2*f_Alpha))

#=====================================================================
#                           Solve 1d-heat
#=====================================================================
#a_x   = np.linspace( .5*f_dx, f_L-.5*f_dx, i_Nx)#np.arange( .5*dx, fL-.5*dx, dx)
a_x    = np.linspace( 0, f_L, i_Nx)
a_t    = np.arange( 0, f_tmax+f_dt, f_dt)
i_Nt   = int(f_tmax/f_dt)+1 # nodes in t
print('space', i_Nx, len( a_x), a_x[1]-a_x[0],    f_dx)
print('time',  i_Nt, len( a_t), round(a_t[1]-a_t[0],2), f_dt)

# IC: aU0 = const ( = 0)
a_U     = np.ones( i_Nx)*f_U0

# make sure that IC and BC match
a_U[0]  = fct_BC_L( 0, f_Uin, f_W)

# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))

#plt.figure(1)
fig, ax1 = plt.subplots( )
for n in range( len(a_t)):# loop over time increments
    ##A##----set BC-----
    a_U[0]  = fct_BC_L( a_t[n], f_Uin, f_W)
    a_U[-1] = fct_BC_L( a_t[n - 1], f_Uout, f_W)
    ##B##-----solve spatial derivatives---------------
    for i in range( 1, i_Nx-1): #spatial loop without boundary nodes
        # central difference solution
        a_dUdt[i] = f_Alpha*((a_U[i+1]-2*a_U[i]+a_U[i-1])/f_dx**2)

    # solve RHS in vectorized form:
    #a_dUdt[1:-1] = f_Alpha*(( a_U[2::] + a_U[0:-2] - 2*a_U[1:-1])/f_dx**2)

    ##C## integration step: forward difference Formula to get u(x,t)
    a_Unew = a_U + f_dt * a_dUdt
    # update the temperature profile for the next time step, otherwise only BC and IC are shown
    a_U    = a_Unew

    ##D## compute exact solution
    a_Uana = fct_u_exact( a_t[n], a_x, f_Alpha, f_Uin, f_W)

#=====================================================================
#               Plot temp. u(x) for every mth time step
#=====================================================================

    print 'time step: ', a_t[n]/(24*3600), 'd' #,(n+1)/plot_step,(n+1)%plot_step
    if (n+1)%plot_step == 0:
        ax1.cla()
        ax1.set_title( 'Time Step: %.2f [d]'%( a_t[n]/(24*3600)))
        ax1.plot( a_U, -a_x, 'ko-', ms = 3, mew =1.5, mfc = 'w', label = 'u(x,t)-num')
        #ax1.plot(  [-f_Uin, f_Uin], [-2*r_diff, -2*r_diff], 'r--', label = '2 x l_diff')
        ax1.plot(  [0,0], [-a_x.max(), 0], '--', color = ' .5')
        # plot exact solution for comparison
        ax1.plot( a_Uana, -a_x, 'r--', lw = 1.5, label = 'u(x,t)-exact')
        ax1.set_xlabel( 'Temperature [degree C]')
        ax1.set_ylabel( 'Depth [m]')
        ax1.legend( loc = 'lower left')
        ax1.set_xlim( -f_Uin-1, f_Uin+1)
        plt.pause( 0.2)

        
#plt.savefig('hw 6 graph')
#=====================================================================
#                               Questions
#=====================================================================
'''
    - 1. You would have to dig about 2.5 meters to totally escape 
    temperature fluctuations. :D
    
    - 2. The expected temperature vatiation is less than one degree at
    2 meters, (Found graphically).
    
    - 3. If you set fAmp = 80, the fluctuations extend to about 3 
    meters down.
'''



