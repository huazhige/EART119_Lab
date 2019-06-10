# -*- coding: utf-8 -*-
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical for resonance

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution (at resonance)
    y(t) = F/(2w0)*t*sin(w0*t)

    comparison of Euler and Runge-Kutta numerical solving methods for ODEs

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
    au_hat    = np.zeros( nSteps) #displacement
    av_hat    = np.zeros( at.shape[0]) #velocity
    #initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        #slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i]
        fn2 = dPar['F']*np.cos(dPar['w']*at[i])-dPar['w0']**2*au_hat[i]
        # Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i]+fn1*dPar['h']
        av_hat[i+1] = av_hat[i]+fn2*dPar['h']
        #alternatively use Euler-Cromer: see Langtangen & Linge, p 129, eq: 4.49 - 4.52
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat

def num_sol_RK( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: ay_hat    - Runge-Kutta
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps) #displacement
    av_hat    = np.zeros( at.shape[0]) #velocity
    
    def dudt(t,v):
        return v
    
    def dvdt(t,u):
        return dPar['F']*np.cos(dPar['w']*t)-dPar['w0']**2*u
    #initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        #slope at previous time step, i. RHS of ODE system
        #have to evaluate u,v simultaniously
        kn1u = dudt(at[i], av_hat[i])
        kn1v = dvdt(at[i], au_hat[i])
        kn2u = dudt(at[i]+0.5*dPar['h'],av_hat[i]+0.5*dPar['h']*kn1v)
        kn2v = dvdt(at[i]+0.5*dPar['h'],au_hat[i]+0.5*dPar['h']*kn1u)
        kn3u = dudt(at[i]+0.5*dPar['h'],av_hat[i]+0.5*dPar['h']*kn2v)
        kn3v = dvdt(at[i]+0.5*dPar['h'],au_hat[i]+0.5*dPar['h']*kn2u)
        kn4u = dudt(at[i]+dPar['h'],av_hat[i]+dPar['h']*kn3v)
        kn4v = dvdt(at[i]+dPar['h'],au_hat[i]+dPar['h']*kn3u)
        
        
        # Runge-Kutta
        au_hat[i+1] = au_hat[i]+( (kn1u + 2*kn2u + 2*kn3u + kn4u)/6)*dPar['h']
        av_hat[i+1] = av_hat[i]+( (kn1v + 2*kn2v + 2*kn3v + kn4v)/6)*dPar['h']
        #alternatively use Euler-Cromer: see Langtangen & Linge, p 129, eq: 4.49 - 4.52
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat
#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
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
            'tStop'  : 20*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)
#the analytical solution
ay_anaRes   = dPar['F']/(2*dPar['w0'])*at*np.sin(dPar['w0']*at)

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
#euler
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#RK
aU_numRK, aV_numRK = num_sol_RK(  at, [dPar['y01'], dPar['y02']], dPar)



#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1) #just analytical solutions
ax = plt.subplot( 211) #plt.axes( [.12, .12, .83, .83])
#ax.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( at,  ay_anaRes, 'r', lw = 1, label = 'ana - resonace')
ax.plot(at, aU_num, 'k--', lw=3, alpha = 0.5, label= 'num - Euler')
ax.plot(at, aU_numRK, 'b--', lw=3, alpha=0.5, label = 'num - RK')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
ax2 = plt.subplot(212) #difference between nummerical and analytical solution
ax2.plot(at, ay_anaRes-aU_num, 'k', lw=3, alpha = 0.5, label= 'error of Euler')
ax2.plot(at, ay_anaRes-aU_numRK, 'b', lw=3, alpha = 0.5, label= 'error of RK')
ax2.set_xlabel( 'Time [s]')
ax2.set_ylabel( 'analyical - numerical solution [mm]')
ax2.legend( loc = 'upper left')
plt.show()
