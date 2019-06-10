# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:11:07 2019

@author: lopez
"""

from __future__ import division
import os 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#--------------my modules----------------------------
#import ODE.ode_utils as utils
"""
Solving for a Second order non homogenous ODE for an undampped, forced oscillator
    using the Runge Kutta method 
    Solving two ODES 
    y(t)'' + ky(t) = f(t)
    f*cos(w*t)     = f(t)
    Analytical Solution
    - y(t) = F/( w0**2 - w**2)*(cos(w*t)- cos(w0*t))
    - We will write a solution as y(t) = sin()*sin()
"""
###########################    FUNCTION DEFENITION   ##########################
def num_sol( at, y0, params):
    """
    at     = time vector 
    y0     = Initial Conditions 
    params = dictionary with set params
    return: ay_hat - fowards Euler method
    """
    nSteps = at.shape[0]# this is to define the start of our time vector and setting it to 1-D 
    #We will create a displacement vector and velocity vector 
    au_hat = np.zeros(nSteps)
    av_hat = np.zeros(at.shape[0])
    #Next we will set initial conditions 
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range(nSteps - 1):
        # slope at previos time steps, i 
        fn1 = av_hat[i]
        fn2 = -dPar['w0']**2*au_hat[i]
        #Eulers Formula y(n+1) = yn +h*f(n)
        au_hat[i+1] = au_hat[i] + dPar['h']*fn1
        av_hat[i+1] = av_hat[i] + dPar['h']*fn2
    return au_hat, av_hat



###########################  Dictionary, files, params #######################
dPar = {# Frequencies
            'w0': .8, #= sqrt(k/m) --> natural frequency
            'w': 1, # --> frequency of forcing function
            'gamma': 0,  
            'F': .5, # Forcing Functions 
            'y0': 0, 'y02': 0,  #Initial Conditions for displacement and velocity 
            #Time steps 
            'h': 1e-2 ,
            'tStart': 0 , 
            'tStop' : 20*np.pi ,           }  
########################### Analytical solutions ###########################
a_t       = np.arange(dPar['tStart'], dPar['tStop'] + dPar['h'], dPar['h'])
fct_t     = dPar['F']*np.cos( dPar['w']*a_t)
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna *a_t
ay_ana1   = -2*(np.sin((dPar['w']*a_t + dPar['w0']*a_t)/2)*np.sin((dPar['w']*a_t - dPar['w0']*a_t)/2))
# envelope - slow frequency
ay_ana2 = -2*preFacAna* ( np.sin( (dPar['w']-dPar['w0'])/2*a_t))
########################### Numerical Solutions ###########################
aU_num, aV_num = num_sol(  a_t, [dPar['y0'], dPar['y02']], dPar)

########################### Plots ###########################
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( a_t, aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( a_t,  ay_ana1, 'r--', lw = 1, label = 'ana - full')
ax.plot( a_t,  ay_ana2,  '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t,  -ay_ana2, '--', color = '.5', lw = 2)
ax.plot( a_t, fct_t, 'b-', lw = 1, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

 
########################### Comparisons ###########################
#We will compare our solutions from Numerical and Analytical methods with the Runge Kutta
#This will be a 4th order Runge Kutta 
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
    Kn1 = fct_RHS( tn , Yn,   params)
    Kn2 = fct_RHS( tn + h*.5, Yn + h*.5*Kn1,  params)
    Kn3 = fct_RHS( tn + h*.5, Yn + h*.5*Kn2,  params)
    Kn4 = fct_RHS( tn + h*.5 ,Yn + h*.5*Kn3,  params)
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
    fn2 = -dPar['w0']**2*u - dPar['gamma']*v # num. params
    return np.array([fn1, fn2])

def num_sol2(at, y0, par):
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
        #forward Euler: y[n+1] = y[n] + fn*h
        #fn1 = av_hat[i]
        #fn2 = -par['w0']**2*au_hat[i]

         #Integration step: Runge Kutta or Euler formula
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat
Au_num = num_sol2(a_t,[dPar['y0'], dPar['y02']],[dPar['tStart'], dPar['tStop']])
print(Au_num)
"""
When I tried to implement the fourth odere runge kutta and tried to plot it alongside the original plots 
I ran into the problem where my parameters didnt fit what I was trying to plot. Based on our code, ODE4, we did in
class it should have allowed me to run num_sol2 because the dictionary used in that script is identical to our dPar. 
I tried first adding the factor of gamma that we were missing but that didnt change much so then I tried to see what 
factors I was misisng or what was named differently but everything seemed right. 
"""
 
 

