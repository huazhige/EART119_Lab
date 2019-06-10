#!/bin/python2.7
"""
Andreas Kooi

g.) When w ~= w0, the function grows with a linear envelope.
h.) y(t) = c1*cos(w0*t) + c2*sin(w0*t) + F/(2*w0)*t*sin(w0*t)
    using I.C.'s y(0) = 0 and y'(0) = 0,
   0 = c1 + 0 + 0
   0 = -0 + w0*c2 + 0 + 0
   c1 = 0
   c2 = 0 
   exact solution:
       y(t) = F/(2*w0)*sin(w0*t)
j.) In reality, the oscillation would have to eventually end since it can't
    keep growing. This would be due to something akin to thermal energy or friction.

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
    au_hat[0] = dPar['y01']
    av_hat[0] = dPar['y02']
    for i in range( nSteps-1):
        # forward Euler or Runge Kutta
        fn1 = av_hat[i]
        fn2 = dPar['F']*np.cos(dPar['w']*a_t[i]) - dPar['w0']**2*au_hat[i]
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1 * dPar['h'] 
        av_hat[i+1] = av_hat[i] + fn2 * dPar['h']
    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------

dPar = {'F': 0.5,
        'w': 1.,
        'w0':1.,
        'tStart': 0,
        'tStop': 20*np.pi,
        'h': 1e-3,
        'y01': 0,
        'y02': 0}


#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
# :TODO  - write down the analyitcal soltuion

ay_ana1   = dPar['F']/(dPar['w0']*2) * a_t * np.sin(dPar['w0']*a_t)
# envelope
ay_ana2 = .25* a_t  

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
ax.plot( a_t,  aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()