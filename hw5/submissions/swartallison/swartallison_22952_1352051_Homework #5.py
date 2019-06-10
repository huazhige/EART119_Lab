# Allison Swart
# Astro/Earth 119 Homework #5
# May 22, 2019

#anaconda2/python2.7

import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Problem 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PART A

def exact_solution( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation 
    by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: 
        ay_hat         - forward Euler
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        fn1 = av_hat[i]
        fn2 = -par['w']**2*au_hat[i]
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']
        #in the case of using Euler-Cromer
        #av_hat[i+1] = av_hat[i] + fn2*par['h']
        #au_hat[i+1] = au_hat[i] + av_hat[i+1]*par['h']
    return au_hat, av_hat

# PART B

dPar = {    # frequencies
            'w0' :   .8, #= sqrt(k/m) --> natural frequency
            'w'  :    1, # --> frequency of forcing function
            # forcing function amplitude
            'F'  : 0.5, #20,
            # initial conditions for displ. and velocity
            'y01' : 0, 'y02' : 0,
            # time stepping
            'h'  : 1e-2,
            'tStart' : 0,
            'tStop'  : 20*np.pi,}

at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])

# forcing function
fct_t     = dPar['F']*np.cos( dPar['w']*at)

# analytical solution
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * fct_t

# PART C

#ay_ana1 = -2*np.sin( (dPar['w'] + dPar['w0']) / 2) * np.sin( (dPar['w'] - dPar['w0']) / 2)
# envelope - slow frequency
ay_ana2 = -2*preFacAna*(np.sin( dPar['w'] - dPar['w0']/2*at))

# PART D

plt.plot( fct_t, 'b-', lw = 3, alpha = .3, label = 'forcing function')
plt.plot( ay_ana1, 'g--', label = 'fast frequency')
plt.plot( ay_ana2, 'r--', label = 'slow frequency')
plt.xlabel( 'Time [sec]')
plt.ylabel( 'Amplitude')
plt.legend( loc = 'upper left')

# PART F

# Forward Euler
def forward_euler( tn, yn, h, fct_t_y, params):
    """
    forward Euler stepper
    :input
                yn    - function value at time tn
                h     - step size
                f_t_y  - function that defines slope at point (t, y)
    :return: 
        yn_hat         - function value at time step tn + h
    """
    fn    = fct_t_y( tn, yn, params)
    yn_hat = yn + fn*h
    return yn_hat

#num_sol = exact_solution( at, dPar['y01'], dPar)
#print num_sol
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
"""

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (2*w0**2)*sin(w0*t)

"""

#-------------------------------0----------------------------------------
#                        params, files, dir
#------------------------------------------------------------------------
dPar = {#frequencies
        'w0' :   1, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, #20,
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 10*np.pi,}

#-----------------------------------1------------------------------------
#                            fct. defintion
#------------------------------------------------------------------------

def num_sol( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: 
        ay_hat    - forward Euler
        ay_hat_rk = 4th order runge kutta
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        fn1 = av_hat[i]
        fn2 = -par['w']**2*au_hat[i] + dPar['F']*np.cos( dPar['w']*at[i])
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']
    return au_hat, av_hat

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------

a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)
ay_ana1   = -2*preFacAna*(np.sin( dPar['w'] - dPar['w0']/2*at))
# envelope
ay_ana2   = preFacAna * a_t

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
ax.plot( aV_num, 'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( aU_num, 'k-', lw = 3, alpha = .3, label = 'num - displ.')
# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  'k--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, 'b--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'k-', lw = 2, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()