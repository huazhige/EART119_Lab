# -*- coding: utf-8 -*-
"""
Inital Value Problem:
    y'' + w0**2 * y = F*cos(w*t)
    F = 0.5, w0 = 0.8; w = 1

a.
    exact solution:
        y= c1 * np.cos(w0*t) + c2 * np.sin(w0*t) + [F/(w0**2 - w**2)*np.cos(w*t)]
b.
    y(0) = 0 = c1*1 + 0 + [F/((w0**2 - w**2))*1]
    y'(0) = 0 = 0 + c2*w0*1 - 0 
    [F/((w0**2 - w**2))*1] = -25/18
    c1 = -[F/((w0**2 - w**2))*1] =  25/18
    c2 = 0
c. y = -25/18 * np.cos(w0*t) - 25/18*np.cos(w*t)\
   y = 25/18 * (2 * sin(t*[w0 + w]/2) * np.sin(t*[w0 - w]/2))

g. When w ~ w0, the function grows with a linear envelope curve.

h. y(t) = c1*cos(w0*t) + c2*sin(w0*t) + F/(2*w0)*t*sin(w0*t)
   y(0) = 0 = c1 + 0 + 0`
   y'(0) = 0 = -0 + w0*c2 + 0 + 0
   c1 = 0
   c2 = 0 
   exact solution:
       y(t) = F/(2*w0)*sin(w0*t)
       
j. In reality I would expect the envelope curve to grow linearly until a 
certain point then taper off to some asymptote.  
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Parameters
# =============================================================================
#Part 1, 
Parr = {'F': 0.5,
        'w': 1.,
        'w0':0.8,
        'tstart': 0,
        'tend': 94.,
        'h': 1e-3,
        'y0': 0,
        'y1': 0}

#Part 2, In phase, w0 = w
phaseParr = {'F': 0.5,
        'w': 1.,
        'w0':1.,
        'tstart': 0,
        'tend': 94.,
        'h': 1e-3,
        'y0': 0,
        'y1': 0}

# =============================================================================
# Functions
# =============================================================================
#time vector
time = np.arange(Parr['tstart'], Parr['tend'], Parr['h'])

#Analitic Solution
def sol_an(time, Parr):
    return Parr['F']/((Parr['w0']**2 - Parr['w']**2)) * \
    (2 * np.sin(time*[Parr['w0'] + Parr['w']]/2) * np.sin(time*[Parr['w0'] - Parr['w']]/2))

def Force(time, Parr):
    return Parr['F']*np.cos(Parr['w']*time)

#Euler's method
def sol_euler(time, Parr):
    nSteps    = time.shape[0]
    au_hat    = np.zeros( nSteps)
    au_hat[0] = Parr['y0']
    av_hat    = np.zeros( time.shape[0])
    av_hat[0] = Parr['y1']
    for i in range( nSteps-1):
        # slope at previous time step, i (these are the right hand sides of the ODEs)
        fn1 = av_hat[i]
        fn2 = Parr['F']*np.cos(Parr['w']*time[i]) - Parr['w0']**2*au_hat[i]
        # euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1 * Parr['h'] 
        av_hat[i+1] = av_hat[i] + fn2 * Parr['h']

    return au_hat, av_hat

#analytic solution for w = w0
def sol_phase_an(time, Parr):
    return Parr['F']/(Parr['w0']*2) * time * np.sin(Parr['w0']*time)
    
# =============================================================================
# Plotting and Calculations
# =============================================================================
#analitic solution w =! w0
au_hat, av_hat = sol_euler(time, Parr)

#analitic solution w = w0
phase_au_hat, phase_av_hat = sol_euler(time, phaseParr)

#plotting for the first part
plt.figure(1)
plt.plot(time, sol_an(time, Parr), 'green') #plotting analytic solution
plt.plot(time, Force(time, Parr), 'dodgerblue', linestyle = 'solid', alpha = 0.5) #plotting forcing function
plt.plot(time, au_hat, 'r-')
plt.legend(["Analytic Solution","Forcing Function","Euler's Method"])
plt.ylabel('y(t)')
plt.xlabel("Time")
plt.savefig('problem 1')
plt.show()


#plotting for the 2nd part
plt.figure(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(time, sol_phase_an(time, phaseParr), 'r-')
ax1.plot(time, phase_au_hat, 'g-')
ax1.legend(["Analytic Solution", "Euler's Method"], loc = 'upper left')
ax1.set_ylabel('y(t)')
ax2.plot(time, sol_phase_an(time, phaseParr) - phase_au_hat)
ax2.set_ylabel('Analytic - Numerical Solution')
ax2.set_xlabel('Time')
plt.savefig('problem 2')
plt.show()






