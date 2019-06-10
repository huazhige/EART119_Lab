#!/bin/python2.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = Ft/( (2*w0**2)*sin(w0*t)


    TODO - compare Euler and Runge-Kutta
    
Summaries/ Responses to problems:
    After plotting the Numerical and analytical solutions to the ODE with w = w0, 
    I found that the two were rather similar when considering frequency and the 
    rate at which their apparent amplitudes grew over time. The two plots differed 
    in terms of their overall amplitude, with the numerical solution having a 
    general amplitude smaller than that of the analytical solution.
    j.) In this case (w =/= w0), it would not be reasonable to assume a linearity 
        between force and displacement, as Hook's Law suggests, since the 
        displacement for this case is greatly increasing over time. This would 
        correspond to a proportionally increasing force, however from the plots 
        we see instead a force that is oscilliatory,
        yet steady in terms of amplitude.

"""
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

#-------------------------------0----------------------------------------
#                   fct. defintion
#------------------------------------------------------------------------
def num_sol( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: ay_hat    - forward Euler
             ay_hat_rk = 4th order runge kutta
    """
    nSteps    = a_t.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( a_t.shape[0])
    # set initial conditions
    au_hat[0] = dPar['y01']
    av_hat[0] = dPar['y02']
    for i in range( nSteps-1):
        # forward Euler or Runge Kutta
        fn1 = av_hat[i] 
        fn2 = dPar['F']*np.cos(dPar['w']*a_t[i]) - dPar['w0']**2*au_hat[i]
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*dPar['h'] 
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']

    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :   .8, #= sqrt(k/m) --> natural frequency
        'w'  :   .8, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-3,
        'tStart' : 0,
        'tStop'  : 10*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
# :TODO  - write down the analyitcal soltuion
ay_ana1   = (dPar['F']*a_t/(dPar['w0'])**2)*np.sin(dPar['w0']*a_t)
# envelope
preFacAna = dPar['F']/(dPar['w0']**2)
ay_ana2   = preFacAna * a_t

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot( 211) #plt.axes( [.12, .12, .83, .83])
plt.title('Undamped HO Numerical Soln. (w = w0): Displacement v. Time' )
ax2 = plt.subplot( 213)
# plot the numerical approximation
ax1.plot( a_t,   aU_num,   'g-', lw = 3, alpha = .3, label = 'num - displ.')
ax1.set_xlabel( 'Time [s]')
ax1.set_ylabel( 'Displacement [mm]')
# analytical solution and envelope fct.
ax2.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax2.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax2.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax2.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax1.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'Displacement [mm]')
ax2.legend( loc = 'upper left')
ax1.legend( loc = 'upper left')
plt.title('Undamped HO Analytical Soln. (w = w0): Displacement v. Time' )
plt.savefig('problem 2')
plt.show()



print 'Summary written in Intro comment within code.'










