#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:01:51 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt

#===================================================
#                  variable library
#===================================================
dPar = {    #frequencies
            'w0' :   1, #= sqrt(k/m) --> natural frequency
            'w'  :   1, # --> frequency of forcing function
            # forcing function amplitude
            'F'  : 0.5, #20,
            # initial conditions for displ. and velocity
            'y01' : 0, 'y02' : 0,
            # time stepping
            'h'  : 1e-2,
            'tStart' : 0,
            'tStop'  : 94,}


#time vector and forcing function
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
fct_t     = dPar['F']*np.cos( dPar['w']*at)

#===================================================
#                 functions
#===================================================   
def ana_sol2(at,dPar):
    return dPar['F']/(dPar['w0']*2) * at * np.sin(dPar['w0']*at)
    
def num_sol( at, y0, dPar):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param dPar :       - dictionary with fct parameters
    :return: ay_hat    - forward Euler
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    #:TODO set the initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i]
        fn2 = dPar['F']*np.cos(dPar['w']*at[i]) - dPar['w0']**2*au_hat[i]
        # Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat

#numerical solutions
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#===================================================
#                 plotting
#===================================================
plt.figure(1)
ax1 = plt.subplot( 211) 
ax2= plt.subplot( 212)
# plot the numerical approximation
ax1.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
# analytical solution
ax2.plot( at,  ana_sol2(at,dPar), 'r--', lw = 1, label = 'ana - full')
ax1.plot( at, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing') #forcing function
ax2.plot( at, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax1.set_xlabel( 'Time [s]')
ax1.set_ylabel( 'Displacement [mm]')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'Displacement [mm]')
ax1.legend( loc = 'upper left')
ax2.legend( loc = 'upper left')
plt.show()
plt.savefig('HW5_2_plot.png')