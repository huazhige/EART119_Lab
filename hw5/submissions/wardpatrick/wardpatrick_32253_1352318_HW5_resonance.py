#!/bin/python2.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m


Q1 Answeres

F  = .5
w0 = .8
w  = 1

a) Exact solution general frorm 
   y = c1 * cos(w0*t) + c2 * sin(w0*t) + [F/(w0**2 - w**2)]*cos(w*t)

b) y(0)  = 0 = c1*1 + 0 + [F/((w0**2 - w**2))*1]
        c1 = -F/(w0**2 - w**2)

   y'(0) = 0 = 0 + c2*w0*1 - 0 
        c2 = 0 

c) y = c1 * cos(w0*t) + [F/(w0**2 - w**2)]*cos(w*t)
   y = c1 * cos(w0*t) + (-c1) *cos(w*t)
   y = c1 * [cos(w0*t) - cos(w*t)]
   
   y = c1 * [-2 * sin((w0+w)/2)*t)*sin((w0-w)/2)*t]


g) When the frequency of the forcing function is in phase with the natural
   frequency of the oscillating system, the amplitude of the displacement continues 
   to increase. 
   
h) y  = c1*cos(w0*t) + c2*sin(w0*t) + F/(2*w0)*t*sin(w0*t)
   y' = -c1*w0*sin(w0*t) + c2*w0*cos(w0*t) + (F/(2*w0))*[sin(w0*t) + t*cos(w0*t)]
   
   y(0)  = 0 = c1 + 0 + 0 
   y'(0) = 0 = 0 + c2*w0 + 0
   
   c1 = 0
   c2 = 0
   
   y = F/(2*w0)*t*sin(w0*t)
   
   
j) In reality, friction would eventually match the driving force and the amplitude 
   would reach a maximum. 
   



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
        # euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1 * dPar['h'] 
        av_hat[i+1] = av_hat[i] + fn2 * dPar['h']
        

    return au_hat, av_hat


def w_w0(time, Parr):
    return dPar2['F']/(dPar2['w0']*2) * a_t * np.sin(dPar2['w0']*a_t)

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :   .8, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 30*np.pi,}


dPar2 = {#frequencies
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
ay_ana22 = .27* a_t  


#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)
aU_num2, aV_num2 = num_sol(  a_t, [dPar2['y01'], dPar2['y02']], dPar)


#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 211) #plt.axes( [.12, .12, .83, .83])
# plot the numerical approximation
ax.plot( a_t,   aU_num,   'g-', lw = 3, alpha = .5, label = 'num - displ.')
# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'k--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax.set_title('w =! w0')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()


ax2 = plt.subplot(212)
ax2.plot( a_t, w_w0(a_t, dPar2) - aU_num2, 'g-', lw = 3, alpha = .5, label = 'num - displ.')
ax2.plot( a_t, w_w0(a_t, dPar2), 'k--', lw = 1, label = 'ana - full')
ax2.plot( a_t,  ay_ana22,  '--', color = '.5', lw = 2, label = 'ana - env')
ax2.plot( a_t,  -ay_ana22, '--', color = '.5', lw = 2)
ax2.plot( a_t, fct_t*8, 'b-', lw = 2, alpha = .5, label ='forcing X 8')



ax2.set_title('w = w0')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'Displacement [mm]')

ax2.legend( loc = 'upper left')
plt.show()









