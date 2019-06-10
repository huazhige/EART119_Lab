#!/bin/python2.7
"""
Andreas Kooi

a.) The exact(analytical) solution
is 
y= c1 * np.cos(w0*t) + c2 * np.sin(w0*t) + [F/(w0**2 - w**2)*np.cos(w*t)]

b.) c1 = 25/18 and c2 = 0, found by:
    using I.C.'s y(0) = 0 and y'(0) = 0,
    0 = c1*1 + 0 + [F/((w0**2 - w**2))*1]
    c1 = -[F/((w0**2 - w**2))*1] = 1.3888 = 25/18
    0 = 0 + c2*w0*1 - 0 
    c2 = 0
    
c.) y(t) = -25/18 * np.cos(w0*t) - 25/18*np.cos(w*t)
    Using the subsitution provided,
    y(t) = - 25/18 * (2 * sin( (w0*t + w*t )/2) * np.sin( (w0*t - w*t )/2))
    
d. and e.) Plotted as requested.

f.) I have noticed that values below h ~ 0.3e-2 produce accurate results
"""

from __future__ import division

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#-------------------------------0----------------------------------------
#                     fct defintion
#------------------------------------------------------------------------
#import ODE.ode_utils as utils

#:TODO - create a python method that solves the ODE system using Runge-Kutta Method

def num_sol( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: ay_hat    - forward Euler
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    #:TODO set the initial conditions
    au_hat[0] = dPar['y01']
    av_hat[0] = dPar['y02']
    for i in range( nSteps-1):
        # TODO: slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i]
        fn2 = dPar['F']*np.cos(dPar['w']*at[i]) - dPar['w0']**2*au_hat[i]
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1 * dPar['h'] 
        av_hat[i+1] = av_hat[i] + fn2 * dPar['h']
        #alternatively use Euler-Cromer: see Langtangen & Linge, p 129, eq: 4.49 - 4.52
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat
#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {    #frequencies
            'w0' :   .8, #= sqrt(k/m) --> natural frequency
            'w'  :   1, # --> frequency of forcing function
            # forcing function amplitude
            'F'  : 0.5, #20,
            # initial conditions for displ. and velocity
            'y01' : 0, 'y02' : 0,
            # time stepping
            'h'  : 1e-2,
            'tStart' : 0,
            'tStop'  : 30*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)
# TODO: write down the analytical solution
c1 = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = c1*np.cos(dPar['w0']*at) - c1*np.cos(dPar['w']*at)
#:TODO rewrite the analytical solution as product of sines

ay_ana1 = -2*c1 * (np.sin(at*[dPar['w0'] + dPar['w']]/2) * np.sin(at*[dPar['w0'] - dPar['w']]/2))

# envelope - slow frequency
ay_ana2 = -2*c1* ( np.sin( (dPar['w']-dPar['w0'])/2*at))

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( at,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( at,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( at,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( at, fct_t, 'b-', lw = 1, alpha = .5, label ='Forcing Function')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()