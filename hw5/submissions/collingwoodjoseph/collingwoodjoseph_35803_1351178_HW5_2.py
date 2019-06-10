#!/bin/python2.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (2*w0**2)*sin(w0*t)


    TODO - compare Euler and Runge-Kutta

"""
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

"""
Question 1(g):
    If the frequency of the forcing function is in phase with the natural
    frequency of the system, then the envelope will increase linearly with
    time.
Question 1(h):
    y = c1*cos(w0t)+c2*cos(w0t)+(F/2w0)*t*sin(w0t)
    0 = c1 + 0 + 0
    0 = 0 + w0*c2 + 0 + 0
    c1 = 0 & c2 = 0
    exact solution: y = (f/2w0)sin(w0t)
Question 1(j):
    Hooke's law is not realistic when w~w0. In reality the envelope should
    increase linearly until it is near an asymptote.
"""

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
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # forward Euler or Runge Kutta
        fn1 = av_hat[i]
        fn2 = par['F']*np.cos(par['w']*at[i]) - par['w0']**2*au_hat[i]
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']
    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :   1, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 10*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
# :TODO  - write down the analyitcal soltuion
preFacAna = dPar['F']/2*dPar['w0']
ay_ana1   = (preFacAna*a_t)*np.sin(dPar['w0']*a_t)
# envelope
ay_ana2   = preFacAna * a_t

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
# plot the numerical approximation
ax.plot( a_t,   aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

#DIFFERENCE BETWEEN NUMERICAL AND ANALYTICAL SOLUTIONS
plt.figure(2)
ax2 = plt.subplot(212)
ax2.plot( a_t, aU_num - ay_ana1, '--', lw = 1, label = 'Num - Ana')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'Displacement [mm]')
ax2.legend( loc = 'upper left')