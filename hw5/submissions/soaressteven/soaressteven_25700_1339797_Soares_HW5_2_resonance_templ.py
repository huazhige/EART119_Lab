#!/bin/python2.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (2*w0**2)*sin(w0*t) )


    TODO - compare Euler and Runge-Kutta

"""
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


#-------------------------------0----------------------------------------
#                         Part g and h
#------------------------------------------------------------------------

# Part g

# If the frequency of the forcing function is in phase with the natural
# frequency then the function will grow linearly over time.

# Part h

# y(0) = 0 = c1*cos(w_0 * 0) + c2 * sin(w_0 * 0) + F/(2 * w_0)*0*sin(w_0*0)
# --> y(0) = c1 + 0 + 0 = c1 --> c1 = 0

# y'(0) = 0 = w_0*c1*sin(w_0 * 0) + w_0*c2*cos(w_0*0) + F*2*w_0*w_0*(sin(w_0*0) 
# + w_0*0*cos(w_0*0)) + -(0*sin(w_0*0))**-2
# --> y'(0) = w_0 * c2 = 0 --> c2 = 0

# This means that the actual solution is
# y(t) = F/((2*w_0)*sin(w_0*t))

# Let's define the actual solution here

def real_sol ( t):
    """
    The real solution derived above
    Params: t - the desired peiod of time
    """
    
    return dPar['F'] / ((2*dPar['w0']) * np.sin(dPar['w0']*t))
    

#-------------------------------1----------------------------------------
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
    au_hat[0] = dPar['y01']
    av_hat[0] = dPar['y02']
    for i in range( nSteps-1):
        # forward Euler or Runge Kutta
        fn1 = av_hat[i]
        fn2 = -par['w']**2*au_hat[i]
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']

    return au_hat, av_hat

#-------------------------------2----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :   1.001, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 10*np.pi,}

#--------------------------------3---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
# :TODO  - write down the analyitcal soltuion
ay_ana1   = dPar['F'] / ( (2 * dPar['w0']**2) * np.sin(dPar['w0']*a_t))
# envelope
ay_ana2   = preFacAna * a_t

#--------------------------------4---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------5---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 211) #plt.axes( [.12, .12, .83, .83])
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
plt.subplot(212) # Part i
plt.plot( a_t,   aU_num,   'k-', lw = 3, alpha = 1, label = 'num - displ.')
plt.plot( a_t, real_sol(a_t), '--', color='green', lw = 3, alpha = .3, label = 'real sol.')
plt.legend(loc = 'upper left')
plt.show()

#--------------------------------6---------------------------------------
#                             Part j
#------------------------------------------------------------------------

# The assumption made in using Hooke's law is still reasonable when w ~ w_0. 
# What happens in reality is that the function grows linearly until it 
# reaches the asymptote, as seen in the part of the function 
# dPar['F']/(dPar['w0']**2 - dPar['w']**2), which shows that when w ~ w_0, 
# there will be a division by zero). At this point, the function will
# no longer grow linearly.