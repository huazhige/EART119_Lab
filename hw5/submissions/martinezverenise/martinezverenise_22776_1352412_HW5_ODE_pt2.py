# -*- coding: utf-8 -*-
"""
We will solve a second order non-homogenous ODE: undampped oscilator 
- We will compare the analytical and numerical soultions 

ODE: m*y''(t) + gy'(t) + ky(t) = F(t)
            w0**2 = k/m
Analytical Solutions:
    y(t) = F/(2*w0**2)*t*sin(w0*t)
We will also compare Euler and Runge Kutta
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
################################ Function defenition ##########################
def num_sol(at, y0, par):
    """
    -solve second order ODE for forced, undamped oscillation by solving two first order ODEs
    ODE:  y''(t) + ky(t) = f(t)
          F*cos(w*t)     = f(t)
    params: y0           - Initial Conditions 
    params: at           - time vector 
    params: par          - Dictionary with fct params
    params: ay_hat       - Foward Eulers Method
    params: ay_hat_rk    - 4th Order Runge Kutta 
    """
    nSteps = at.shape[0]
    au_hat = np.zeros(nSteps)
    av_hat = np.zeros(at.shape[0])
    #SET INTITIAL CONDITIONS
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range (nSteps - 1):
        fn1 = av_hat[i]
        fn2 = -par['w0']**2*au_hat[i] + dPar['F']*np.cos(dPar['w']*at[i])
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat
################################ Params and files ################################
dPar = { #Frequencies 
        'w0': .8, #Natural Frequency 
        'w' : .8,  #Frequency of forcing Function  
        #Force Function 
        'F' : .5, 
        #Intitial Conditions for displacement and velocity 
        'y0': 0, 'y02':0,
        #Time steps 
        'h' : 1e-2,
        'tStart': 0,
        'tStop' : 10*np.pi, }
######################### Analytical Solutions ###############################
a_t = np.arange(dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
# Forcing Function 
fct_t = dPar['F']*np.cos(dPar['w']*a_t)
#Writing down analytical solution 
ay_ana1   = dPar['w0']*np.cos(dPar['w0']*a_t) + (dPar['F']*a_t*np.cos(dPar['w0']*a_t))/2
# y(t) = F/(2*w0**2)*t*sin(w0*t)
preFacAna = dPar['F']/(2*dPar['w0']**2)#*np.sin(dPar['w0']*a_t)
# Envelope 
ay_ana2   = preFacAna * a_t 
############################  Numerical Soultions ############################
aU_num, aV_num = num_sol( a_t, [dPar['y0'], dPar['y02']], dPar)
############################        PLOTS       ###############################
plt.figure(1)
ax = plt.subplot( 111)
#plt.axes( [.12, .12, .83, .83])
#plot the numerical approximation
ax.plot( a_t, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
#analytical solution and envelope fct.
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()
###########################  Extra Notes ##################################
"""
part(g) If the forcing frequency is in phase with the natural frequency then based on our results 
we can see tha the blue line(forcing function) affects both the numerical displacement and anylitical
solutions(Velocity). If we were to change the value of w0 and w we would have a different diagram that 
would be dependent on the forcing function.

part(J) The reason why it doesnt seem realistic to use w0 ~ w is because we assummed that velocity 
and displacement are linear when in real life applications velocity could be changing at a certain rate.  

"""


















