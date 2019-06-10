#!/bin/python2.7
"""
HW #5 PROBLEM 1

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (w0**2 - w**2)*( cos(w*t) - cos(w0*t) )
    - solution as product of sines
    y(t) = (-2*F/(w0**2 - w**2)) * sin((w*t + w0*t)/2)* sin((w*t - w0*t)/2)

@author: scarletpasser
"""
import matplotlib.pyplot as plt
import numpy as np
#-------------------------------------------------------------------------
#                            Summery 
#------------------------------------------------------------------------
'''
    The oscillator in question is both forced and damped, meaning that 
    there is an external force which contributes to oscillations, and because
    the system is undamped, the external force is not required to maintain
    oscillations. If you change the amplitude of the force function, 
    it changes the displacement of the solution, with a large 'F' giving more 
    displacement and small 'F's giving less displacement. In the graph you
    can also see that the forcing funciton is out of phase with the solutions,
    which makes sense because in this case, w != w0. Visually, you can also 
    observe from the graph that the error seems to worsen with time, with the
    difference between the analytical and the numerical solutions looking
    bigger farther down the time axis.
    
'''
#-----------------------------------------------------------------------
#                     fct defintion
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
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    #initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        #slope at previous time step, i. RHS of ODE system
        fn1 = av_hat[i] 
        fn2 = -par['w']**2*au_hat[i] + par['F']*np.cos(par['w0'] * i * par['h'])
        #Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']
    return au_hat, av_hat

#-----------------------------------------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = {    #frequencies
            'w0' :   .8, #= sqrt(k/m) --> natural frequency
            'w'  :   1, # --> frequency of forcing function
            # forcing function amplitude
            'F'  : 0.5,
            # initial conditions for displ. and velocity
            'y01' : 0, 'y02' : 0,
            # time stepping
            'h'  : 1e-2,
            'tStart' : 0,
            'tStop'  : 20*np.pi,}

#-----------------------------------------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])

# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)

#analytical solution - found with pen and paper 
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * -2 * np.sin((dPar['w']*at + dPar['w0']*at)/2) * np.sin((dPar['w']*at - dPar['w0']*at)/2)

#envelope - slow frequency
ay_ana2 = -2*preFacAna* ( np.sin( (dPar['w']-dPar['w0'])/2*at))

#-----------------------------------------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  at, [dPar['y01'], dPar['y02']], dPar)

#-----------------------------------------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])

#numerical solution plot: 
ax.plot( at, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')

#analytical solution plot: 
ax.plot( at,  ay_ana1, 'r--', lw = 1, label = 'ana - full')

#slow frequency plot: 
ax.plot( at,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( at,  -ay_ana2, '--', color = '.5', lw = 2)

#Forcing function plot 
ax.plot( at, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing')

####Labels###
plt.title('Forced/undamped oscillations')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

#plt.savefig('HW 5 graph 1')

