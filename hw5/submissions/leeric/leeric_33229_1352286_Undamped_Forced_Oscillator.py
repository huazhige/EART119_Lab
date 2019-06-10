# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:39:33 2019
Homework 5 Undamped Forced Oscillator
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt

#======================================================================
#               Parameters
#======================================================================
y0 = 0
y_prime = 0
F0 = 0.5
w0 = 0.8
w = 1

#for y(0) = 0 and y'(0) = 0
c1 = F0/(w**2 - w0**2)
c2 = 0

#a_t = np.linspace(dPar['tStart'], dPar['tStop'], 1000)

dPar = { #frequencies
        'w0'    :  .8, #= sqrt(k/m) --> natural frequency
        'gamma' :   0.2, # damping constant, set to 0 to compare to exact solution
        # initial conditions for displ. and velocity
        'w' : 1,
        'y01' : 0,
        'y02' : 0,
        # time stepping
        'h'      : 1e-2,
        'tStart' : 0,
        'tStop'  : 20*np.pi,}

at = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])



#========================================================================
#               import functions
#========================================================================
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
    fn1 = v #u-prime
    fn2 = F0*(np.cos(dPar['w']*t))-(par['w0']**2)*u #v-prime
    return np.array([fn1, fn2])

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
    Kn1 = fct_RHS( tn,  Yn, params)
    Kn2 = fct_RHS( tn + h/2, Yn +.5*h*Kn1,  params)
    Kn3 = fct_RHS( tn + h/2, Yn + .5*h*Kn2,  params)
    Kn4 = fct_RHS( tn + h, Yn + h*Kn3,  params)
    return (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)/6

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
    euler_au_hat    = np.zeros( nSteps)
    euler_av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    euler_au_hat[0] = y0[0]
    euler_av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step, i
        fn1, fn2     = runge_kutta_vec( at[i], np.array([au_hat[i], av_hat[i]]), oscillator, par)
        #forward Euler: y[n+1] = y[n] + fn*dPar['h']
        fn3, fn4 = oscillator(at, [euler_au_hat, euler_av_hat], par)

        # Integration step: Runge Kutta or Euler formula
        au_hat[i+1] = au_hat[i] + par['h']*fn1
        av_hat[i+1] = av_hat[i] + par['h']*fn2
        
        euler_au_hat[i+1] = euler_au_hat[i] + par['h']*fn3[i]
        euler_av_hat[i+1] = euler_av_hat[i] + par['h']*fn4[i]
    return au_hat, av_hat, euler_au_hat, euler_av_hat

#=====================================================================
#       Functions
#=====================================================================

#general solution in terms of sines
def position(t, par):
    return (F0/(par['w0']**2 - par['w']**2))*(-2)*(np.sin((par['w']+par['w0'])\
                *t/2)*np.sin((par['w']-par['w0'])*t/2))
y = position(at, dPar)

#driving force
def force(t):
    return (F0/(w0**2 - w**2))*np.cos(w*t)
f_t = force(at)

#numerical solutions
u_runge_kutta, v_runge_kutta, u_euler_method, v_euler_method = \
num_sol(at, [dPar['y01'], dPar['y02']], dPar)


#======================================================================
#               Resonance
#======================================================================
def res_postion(at, par):
    return (F0/(2*par['w0']))*at*np.sin(par['w0']*at)

resonance_dictionary = { 'w0'    :  1,
        'w' : 1,
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'      : 1e-2,
        'tStart' : 0,
        'tStop'  : 20*np.pi,}
y_res = res_postion(at, resonance_dictionary)
res_u_runge_kutta, res_v_runge_kutta, res_u_euler_method, res_v_euler_method =\
num_sol(at, [dPar['y01'], dPar['y02']], resonance_dictionary)
#======================================================================
#           Plotting
#======================================================================
plt.figure(1)
plt.title("Undamped, Forced Oscillator")
plt.plot(at, y, "r-", label = "Undamped Forced Osillator")
plt.plot(at, f_t, "b--", label = "Driving Force", alpha = .5)
plt.legend()
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("y-position")
plt.show()

plt.figure(2)
plt.title("Euler's Method vs Exact")
plt.plot(at, u_euler_method, "b--", label = "Euler's Method")
plt.plot(at, y, "r--", label = "Analytical Solution")
plt.legend()
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("y-position")
plt.show()

plt.figure(3)
plt.title("Runge Kutta vs Exact")
plt.plot(at, u_runge_kutta, "b--", label = "Runge Kutta")
plt.plot(at, y, "r--", label = "Analytical Solution")
plt.grid(True)
plt.legend()
plt.xlabel("Time")
plt.ylabel("y-position")
plt.show()

plt.figure(4)
plt.title("Resonance with Runge Kutta")
exact = plt.subplot(211)
exact.grid(True)
exact.plot(at, y_res, "r--", label = "exact solution")
exact.legend()
plt.xlabel("Time")
plt.ylabel("y-position")
num_runge_kutta = plt.subplot(212)
num_runge_kutta.grid(True)
num_runge_kutta.plot(at, res_u_runge_kutta, label = "runge kutta")
plt.xlabel("Time")
plt.ylabel("y-position")
num_runge_kutta.legend()
plt.show()

plt.figure(5)
plt.title("Resonance with Euler Method")
exact2 = plt.subplot(211)
exact2.grid(True)
exact2.plot(at, y_res, "r--", label = "exact solution")
exact2.legend()
plt.xlabel("Time")
plt.ylabel("y-position")
num_euler_method = plt.subplot(212)
num_euler_method.grid(True)
num_euler_method.plot(at, res_u_euler_method, label = "euler_method")
num_euler_method.legend()
plt.xlabel("Time")
plt.ylabel("y-position")
plt.show()

#The resonance plot is not realistic. As time goes on, it assumes that the 
#amplitude would continue to grow. I believe that, at some x, there should
#be an extra tension force that restricts that amplitude from increasing.


