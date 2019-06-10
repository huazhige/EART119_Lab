#!/bin/python2.7
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (w0**2 - w**2)*( cos(w*t) - cos(w0*t) )
    :TODO -
    y(t) = 25/18 * (2 * sin(t*[w0 + w]/2) * np.sin(t*[w0 - w]/2))


    TODO - compare Euler and Runge-Kutta

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
def sol_an(time, Parr):
    return Parr['F']/((Parr['w0']**2 - Parr['w']**2)) * \
    (2 * np.sin(time*[Parr['w0'] + Parr['w']]/2) * np.sin(time*[Parr['w0'] - Parr['w']]/2))

def Force(time, Parr):
    return Parr['F']*np.cos(Parr['w']*time)
#:TODO - create a python method that solves the ODE system using Runge-Kutta Method
Parr = {'F': 0.5,
        'w': 1.,
        'w0':0.8,
        'tstart': 0,
        'tend': 94.,
        'h': 1e-3,
        'y0': 0,
        'y1': 0}
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
    au_hat[0] = Parr["y0"]
    av_hat[0] = Parr["y1"]
    for i in range( nSteps-1):
        # TODO: slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i]
        fn2 = Parr['F']*np.cos(Parr['w']*t[i]) - Parr['w0']**2*au_hat[i]
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1 * Parr['h']
        av_hat[i+1] = av_hat[i] + fn2 * Parr['h']
        #alternatively use Euler-Cromer: see Langtangen & Linge, p 129, eq: 4.49 - 4.52
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat

t = np.linspace(Parr['tstart'], Parr['tend'], 6285)
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
            'tStop'  : 20*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)
# TODO: write down the analytical solution
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * ( np.cos(dPar["w"]*t) - np.cos(dPar["w0"]*t) )
#:TODO rewrite the analytical solution as product of sines
#ay_ana1 = -25/18 * (2 * np.sin(t*[dPar["w0"] + dPar["w"]/2]) * np.sin(t*[dPar["w0"] - dPar["w"]/2]))
# envelope - slow frequency
ay_ana2 = -2*preFacAna* ( np.sin( (dPar['w']-dPar['w0'])/2*at))

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
plt.plot(t, ay_ana1, 'green') #plotting analytic solution
#
plt.plot(t, Force(t, Parr), 'dodgerblue', linestyle = 'solid', alpha = 0.5) #plotting forcing function
plt.plot(t, aU_num, 'r-')
plt.legend(["Analytic Solution","Forcing Function","Euler's Method"])
plt.ylabel('y(t)')
plt.xlabel("Time")
#plt.savefig('problem 1')
plt.show()
