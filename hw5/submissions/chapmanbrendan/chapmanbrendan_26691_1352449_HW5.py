# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#===================================================================================
#                                Packages
#===================================================================================
from __future__ import division
import os
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                                Variables
#===================================================================================
m = 1

yp = 0
F = 0.5
w = 1
t = 0
w0 = 0.8



"""
###############################################################################
Question 1
###############################################################################
"""
#===================================================================================
#                                define fct.
#===================================================================================




def y(c1, o0, t, c2, F, o,):
    return c1*np.cos(o0*t) + c2*np.sin(o0*t) + ((F/(o0**2-o**2))*np.cos(o*t))
c1 = 2                
c2 = 3
y =	c1*np.cos(w0*t) + c2*np.sin(w0*t) + (F/(w0**2- w**2))*np.cos(w*t)

#===================================================================================
#                          Solving
#===================================================================================

 

"b."
c1 = (c2*np.sin(w0*t) + (F/(w0**2- w**2))*np.cos(w*t))/np.cos(w0*t)
c2=  ((((F/(w0**2-w**2))*np.cos(w*t)) +c1*np.cos(w0*t))/ np.sin(w0*t))
print(c1)
print(c2)

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
    au_hat[0] = 0
    av_hat[0] = 0
    for i in range( nSteps-1):
        # TODO: slope at previous time step, i. RHS of ODE system
        fn1 = au_hat
        fn2 = av_hat
        # TODO: -  Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = y
        av_hat[i+1] = yp
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
            'tStop'  : 20*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
fct_t     = dPar['F']*np.cos( dPar['w']*at)
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * ( 43)


"c.  rewrite the analytical solution as product of sines"
ay_ana1 = -fct_t * ( np.sin( 43)  * np.sin(43))
# envelope - slow frequency
ay_ana2 = -2*preFacAna* ( np.sin( (dPar['w']-dPar['w0'])/2*at))

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
"d, e."

plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( at,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( at,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( at,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( at, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()


"""
###############################################################################
Question 2
###############################################################################
"""

"g."
"The amplitude increases by 100%"


"h."





"i."  
plt.figure(1)
ax = plt.subplot( 212) #plt.axes( [.12, .12, .83, .83])
ax.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( at,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( at,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( at,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( at, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

"j." 
"No, in reality instabilities in the transfer of energy would compound, leading to a phase disequilibrium."
#===================================================================================
#                                Variables
#===================================================================================


#===================================================================================
#                          Solving
#===================================================================================
