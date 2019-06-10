#!/bin/python3.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (2*w0**2)*sin(w0*t)


    TODO - compare Euler and Runge-Kutta
    
    
 II)
    g) When the forcing frequency is the same as the natural frequency of the system
    it is in "resonance" and the amplitude of the function will increase.
    
    h) Exact solution for w = w0:
        y = c1*cos(w0*t) + c2*sin(w0*t) + [F/2*w0]*t*sin(w0*t)
    
    j) In reality linearity between force and change in displacement is not realistic
        at resonance. Usually when things are oscillating they reach a maximum displacement
        before whatever is oscillating breaks or a force starts slowing it down. (Example
        of a maximum oscillation is the Tacoma narrows bridge that was destroyed when the
        driving force was at or near resonance.)
    


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

        au_hat[i+1] = au_hat[i] + fn1 * dPar['h'] 
        av_hat[i+1] = av_hat[i] + fn2 * dPar['h']
    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :  0.8, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 30*np.pi,}

dPar1 = {#frequencies
        'w0' :   1, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
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
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
# :TODO  - write down the analyitcal soltuion
ay_ana1   = dPar['F']/((dPar['w0']**2 - dPar['w']**2)) * \
    (2 * np.sin(a_t*[dPar['w0'] + dPar['w']]/2) * np.sin(a_t*[dPar['w0'] - dPar['w']]/2))
# envelope
#ay_ana2   = preFacAna * a_t
ay_ana2 = 3.1 * np.sin(a_t*[dPar['w0'] - dPar['w']]/2)
ay_ana3 = .27* a_t

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)
aU_num2, aV_num2 = num_sol(  a_t, [dPar1['y01'], dPar1['y02']], dPar1)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
fig = plt.figure(1)


ax = fig.add_subplot( 211) #plt.axes( [.12, .12, .83, .83])
# plot the numerical approximation
ax.plot( a_t,   aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')



# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
#ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')


ax2 = fig.add_subplot(212)
ax2.plot( a_t, (dPar1['F']/(dPar1['w0']*2) * a_t * np.sin(dPar1['w0']*a_t)) - aU_num2, 'r-', lw = 3, alpha = .5, label = 'numerical')
ax2.plot( a_t, dPar1['F']/(dPar1['w0']*2) * a_t * np.sin(dPar1['w0']*a_t), 'k--', lw = 1, label = 'analytical')
ax2.plot( a_t,  ay_ana3,  '--', color = '.5', lw = 2, label = 'Envelope')
ax2.plot( a_t,  -ay_ana3, '--', color = '.5', lw = 2)
ax2.plot( a_t, fct_t*8, 'b-', lw = 2, alpha = .5, label ='forcing')

ax2.set_title('w = w0')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'Displacement [mm]')

ax2.legend( loc = 'upper left')

plt.show()