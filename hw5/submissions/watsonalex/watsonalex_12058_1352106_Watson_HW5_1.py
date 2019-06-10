#!/bin/python2.7
"""
Homework 5 Part 1
Alex Watson
solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (w0**2 - w**2)*( cos(w*t) - cos(w0*t) )
    :TODO - write solution as product of sines
    y(t) = sin * sin

    TODO - compare Euler and Runge-Kutta

    --SUMMARY OF OBSERVATIONS AT THE BOTTOM--
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
    -  solve second order ODE for forced, 
    undamped oscillation by solving two first order ODEs
    ODE: y''(t) + ky(t) = f(t)
    f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :- time vector
    :param par :       - dictionary with fct parameters
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
        # TODO: slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i]
        fn2 = -par['w0']**2*au_hat[i] + par['F']*np.cos( par['w']*at[i])
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + par['h']*fn1
        av_hat[i+1] = av_hat[i] + par['h']*fn2
        #alternatively use Euler-Cromer: see Langtangen & Linge, p 129, eq: 4.49 - 4.52
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat

def runge_kutta_vec( tn, Yn, fct_RHS, params):
    """
    fourth order runge kutta stepper, for single or system of  ODEs
    :input       tn           - current time step
                 Yn           - function value at time tn
                 fct_RHS      - vectorised function that defines slope (derivative) at point (t, y)
                                = all RHS of the system of ODEs

                 params   - py dictionary that includes step size 'h'
                            and all parameters needed in function:
                            fct_RHS

    :return: a_fn1 - values of derivatives at current tn for all ODEs
    """
    h = params['h']
    Kn1 = fct_RHS( tn, Yn, params)
    Kn2 = fct_RHS( tn + 0.5*h, Yn + 0.5*h*Kn1, params)
    Kn3 = fct_RHS( tn + 0.5*h, Yn + 0.5*h*Kn2, params)
    Kn4 = fct_RHS( tn + h, Yn + h*Kn3, params)
    return (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)/6

def oscillator( t, Yn, par):
    """
    - describe second order ODE for forced, undamped oscillation by two first order ODEs
        ODE:  y''(t) + w0**2y(t) = f(t)
                                f(t) = F*cos(w*t)
             u   =  y; v = y'
             u'  =  v
             v'  = -k*u + f(t)
    :input - t - time vector
             u  - displacement
             v  - velocity
             F  - amplitude of forcing fct
             w0 -  parameter: natural fequency: w0**2 = k/m

    :return:  [displ, vel]
    """
    u, v = Yn[0], Yn[1]
    fn1 = v
    fn2 = -par['w0']**2*u + par['F']*np.cos( par['w']*t)
    return np.array([fn1, fn2])

def num_sol_RK( at, y0, par):
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
        # slope at previous time step, i
        fn1, fn2     = runge_kutta_vec( at[i], np.array([au_hat[i], av_hat[i]]), oscillator, dPar)
        # forward Euler: y[n+1] = y[n] + fn*h
        #fn1 = av_hat[i]
        #fn2 = -par['w0']**2*au_hat[i]

        # Integration step: Runge Kutta or Euler formula
        au_hat[i+1] = au_hat[i] + par['h']*fn1
        av_hat[i+1] = av_hat[i] + par['h']*fn2
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
            'h'  : 1e-3, #BONUS: changed time step to give more accurate fit for Euler num. approx (orig 1e-2)
            'tStart' : 0,
            'tStop'  : 30*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)
# TODO: write down the analytical solution
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * ( np.cos( dPar['w']*at) - np.cos( dPar['w0']*at))
#:TODO rewrite the analytical solution as product of sines
ay_ana1 = -2*preFacAna * ( np.sin( ( at*( dPar['w'] + dPar['w0']))/2)  
                           * np.sin( ( at*( dPar['w'] - dPar['w0']))/2))
# envelope - slow frequency
ay_ana2 = -2*preFacAna* ( np.sin( (dPar['w']-dPar['w0'])/2*at))

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num       = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)
##BONUS Runge Kutta##
aU_num_RK, aV_num_RK = num_sol_RK( at, [dPar['y01'], dPar['y02']], dPar)
#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
plt.title( 'Forced, Undampened Oscillating System (w0 /= w)')
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( at, aU_num,    'k-', lw = 3, alpha = .3, label = 'num - displ. (Euler)')
ax.plot( at, aU_num_RK, 'g-', lw = 3, alpha = .4, label = 'num - displ. (Runge Kutta)')
ax.plot( at,  ay_ana1,  'r--', lw = 1, label = 'ana - full')
ax.plot( at,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( at,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( at, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

"""
our observations show that a forced, undampened system with a difference between
w and w0 will increase and decrease in amplitude over time in a cycle.

    - The Euler numerical approximation becomes less and less accurate/propagates over time,
      compared to the analytical approximation
          - BONUS: This propagation minimizes as the time steps are made smaller. 
            Any time step lower than 1e-3 results in very little innaccuracy
    
    - BONUS: The RK numerical approximation is almost the same as the analytical solution, 
      which shows that it is more accurate / better suited for this kind of scenario

"""