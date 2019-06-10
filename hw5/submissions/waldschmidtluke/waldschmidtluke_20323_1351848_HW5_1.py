#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:26:10 2019

@author: lukewaldschmidt
"""
import numpy as np
import matplotlib.pyplot as plt

#===================================================
#                  variable library
#===================================================

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
            'tStop'  : 94,}


#time vector and forcing function
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
fct_t     = dPar['F']*np.cos( dPar['w']*at)

#===================================================
#                 functions
#===================================================

def ana_sol1(at,dPar): 
    return dPar['F']/((dPar['w0']**2 - dPar['w']**2)) * \
    (2 * np.sin(at*[dPar['w0'] + dPar['w']]/2) * np.sin(at*[dPar['w0'] - dPar['w']]/2))

def ana_sol1slow(at,dPar):
    return dPar['F']/((dPar['w0']**2 - dPar['w']**2)) * \
    (2 * np.sin(at*[dPar['w0'] - dPar['w']]/2) * np.sin(at*[dPar['w0'] - dPar['w']]/2))
    
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

#numerical solution
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)


#===================================================
#                  plotting
#===================================================

plt.figure(1)
ax = plt.subplot( 111)
plt.plot(at, ana_sol1(at, dPar), 'r--', lw = 1, label = 'ana - full') #analytic solution
plt.plot(at, ana_sol1slow(at, dPar), 'k--', lw = 1, label = 'ana - full -slow') #analytic solution (slow freq)
plt.plot(at, -ana_sol1slow(at, dPar), 'k--', lw = 1)
plt.plot(at, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing') #forcing function
plt.plot(at, aU_num, 'g-', lw = 3, alpha = .3, label = 'num - displ.') #numerical solution
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()
plt.savefig('HW5_1_plot.png')
