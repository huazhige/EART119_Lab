#!/bin/python2.7
"""
Homework 5 Part 2
Alex Watson
solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/(2*w0**2)*t*sin(w0*t)


    TODO - compare Euler and Runge-Kutta

    --SUMMARY OF OBSERVATIONS AT BOTTOM--

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
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        fn1 = av_hat[i]
        fn2 = -par['w0']**2*au_hat[i] + par['F']*np.cos( par['w']*at[i])
        # forward Euler or Runge Kutta
        au_hat[i+1] = au_hat[i] + par['h']*fn1
        av_hat[i+1] = av_hat[i] + par['h']*fn2

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
ay_ana1   = dPar['F']/(2*dPar['w0']**2)*a_t*np.sin(dPar['w0']*a_t)
# envelope
preFacAna = dPar['F']/(2*dPar['w0']**2)
ay_ana2   = preFacAna * a_t

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
plt.title( 'Forced, Undampened Oscillating System (w0 = w)')
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

"""
When w = w0, the entire oscillating system's amplitude increases over time in a linear fashion
    - Amplitude increase = ay_ana2 = a_t*F/(2*w0**2)
    
    - The Euler numerical method propagates/ becomes more inaccurate over time, similar to Part 1.
      This would likely be minimized with smaller time steps as well
    
    - In reality, the system would not keep linearly increasing like it does in this coded scenario.
      The amplitude of the system would reach a maximum of some kind. For example, in a mass-spring oscillation system,
      the max amplitude would be related to the max lenth of the spring and its maximum elasticity. Nothing in the world
      would physically keep increasing as it would run out of energy as well.
"""
