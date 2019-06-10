#!/bin/python2.7
"""
HW #5 PROBLEM 2

solve second order, non-homogeneous ODE: undamped harmonic oscillator

- compare analytical and numerical

ODE: my''(t) + gy'(t) + ky(t) = f(t)
        w0**2 = k/m

ana. solution:
    y(t) = F/( (2*w0**2)*sin(w0*t)

@author: scarletpasser
"""

import matplotlib.pyplot as plt
import numpy as np
#-------------------------------------------------------------------------
#                            Summery 
#------------------------------------------------------------------------
'''
    Identical to the previous problem, this problem deals with an undamped 
    and forced harmonic oscillator. However, unlike before, this 
    oscillator has a natural frequency that is in phase with the 
    frequency of the forcing funciton. Because of this, the amplitude of 
    the oscillations increase with time, sort of like there is 
    continues constructive interference between the forcing funciton and
    the harmonic oscillator. This is evident in the graph, with the 
    amplitude of the oscillations increasing with time. You can also see
    in the graph that the error between the numerical and analytical 
    solution gets worse over time, similar to problem one. 

'''
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
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        fn1 = av_hat[i] + au_hat[0]
        fn2 = -par['w']**2*au_hat[i] + par['F']*np.cos(par['w0'] * i * par['h']) 
        # Euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']

    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
#in this case w0 = w
dPar = {#frequencies
        'w0' :   1, #= sqrt(k/m) --> natural frequency
        'w'  :   1, # --> frequency of forcing function
        # forcing function
        'F'  : 0.5, 
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'  : 1e-2,
        'tStart' : 0,
        'tStop'  : 10*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
#Time vector 
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])

# forcing function: 
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)

#analyitcal soltuion: 
preFacAna = dPar['F'] / (2*dPar['w0'])
ay_ana1   = preFacAna * np.sin(dPar['w0'] * a_t) * a_t

# envelope
ay_ana2   = preFacAna * a_t

#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

# difference between numerical and anaylitical solutions
dif = aU_num - ay_ana1
#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)


ax = plt.subplot( 211) #plt.axes( [.12, .12, .83, .83])

# plot of the numerical approximation:
ax.plot( a_t, aU_num,  'k-', lw = 3, alpha = .3, label = 'num - displ.')

# analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)

# forcing function
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
plt.title('Forced/damped oscillation (w0 = w)')

# difference graph 
plt.subplot(212)
plt.plot(a_t, dif,    'r',                       label = 'difference')
plt.plot(a_t, ay_ana1,'b--', lw = 1,             label = 'ana - full')
plt.plot(a_t, aU_num, 'k',   lw = 3, alpha = .3, label = 'num - displ.')
plt.ylabel('Difference [mm]')
plt.legend(loc = 'upper left')

####Labels###
plt.title('Diff b/n Numerical and Analytical solution')
plt.xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

#plt.savefig('HW 5 graph 2')

#-----------------------------------------------------------------------
#                            In reality...
#------------------------------------------------------------------------
'''
    Accrording to the solution, displacement increases as time goes on. 
    Hooke's law states that F = -kx, with x being displacement. In 
    reality though, there are probably some limitations on this. My gut 
    says that perhaps if the displacement were big enough, MORE force 
    would be required to achieve the previously linear displacement. 
    And in this problem specifically, unless our oscillator extended to 
    infinity, there would have to be some limit on the displacement 
    as well. 
    
'''
