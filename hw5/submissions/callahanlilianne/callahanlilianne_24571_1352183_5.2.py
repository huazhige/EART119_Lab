"""
Lili Callahan

Homework 5, Problem 2:
Solve second order, non-homogeneous ODE: undamped harmonic oscillator
Compare analytical and numerical solutions
This time, w0 = w = 1

ODE: 
    my''(t) + gy'(t) + ky(t) = f(t)
    w0**2 = k/m

Analytical solution:
    y(t) = F*t/(2*w0)*sin(w0*t)

"""
###########################################################################
#       Part g)
###########################################################################

"""
When the frequency of the forcing function is in phase with the 
natural frequency of the oscillating system (w ~ w0) the system experiences resonance. 
This causes the oscillations to continuously increase in magnitude. 

"""

import matplotlib.pyplot as plt
import numpy as np


###########################################################################
#       Dictionary and Parameters
###########################################################################

dPar = { # frequencies
         'w0'     :   1, # --> sqrt(k/m) --> natural frequency
         'w'      :   1, # --> frequency of forcing function
         # forcing function
         'F'      : 0.5,
         # initial conditions for displ. and velocity
         'y01'    : 0, 'y02' : 0,
         # time stepping
         'h'      : 1e-2,
         'tStart' : 0,
         'tStop'  : 10*np.pi,}

###########################################################################
#       Analytical Solution: Part h)
###########################################################################

# time variable
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])

"""
Constants:
    c1 = 0
    c2 = 0
"""

# forcing function
fct_t     = dPar['F']*np.cos( dPar['w0']*a_t)

# analytical solution
preFacAna = dPar['F']/(2*dPar['w0'])
ay_ana1   = preFacAna*np.sin(dPar['w0']*a_t)*a_t

# slow frequency
ay_ana2   = preFacAna * a_t

###########################################################################
#       Numerical Solution: Part h)
###########################################################################

def num_sol( at, y0, par):
    """
    Solve second order ODE for forced, undamped oscillation by solving two first order ODEs
    ODE:  
        y''(t) + ky(t) = f(t)
        f(t) = F*cos(w*t)
    
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step
        fn1 = av_hat[i]
        fn2 = -par['w']**2*au_hat[i] + dPar['F']*np.cos(dPar['w']*i*dPar['h'])
        # euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat

aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)

###########################################################################
#       Plotting: Parts h) and i)
###########################################################################

plt.figure(1)
ax = plt.subplot(211)
# numerical solution for comparison
ax.plot( a_t, aU_num, 'k-', lw = 3, alpha = .3, label = 'num - displ.')
# analytical solution: fast frequency
ax.plot( a_t, ay_ana1, 'r--', lw = 1, label = 'ana - full')
# analytical solution: slow frequency
ax.plot( a_t, ay_ana2, '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot( a_t, -ay_ana2, '--', color = '.5', lw = 2)
# forcing function
ax.plot( a_t, fct_t, 'b-', lw = 2, alpha = .5, label ='forcing')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()

# plotting difference between analytical and numerical
diff = aU_num - ay_ana1
plt.subplot(212)
plt.plot(a_t, diff, label = 'diff between ana and num')
plt.xlabel( 'Time [s]')
plt.ylabel( 'Displacement [mm]')
plt.legend( loc = 'upper left')
plt.show()
plt.savefig('5.2_plot.png')

###########################################################################
#       Part j)
###########################################################################

"""
According to Hooke's Law, more force is needed to create more displacement, which creates a 
linear relationship between the two. This is not the reality when w = w0. In the
graph of the solution, displacement increases without a further increase in force. 
In reality, the displacement would only increase until a damping force like air 
resistence stopped the object from oscillating forever.

"""

###########################################################################
#       Observations
###########################################################################

"""
Since the object is oscillating at its resonant frequency, w = w0, it's displacement
continuously increases. In this problem, there is no damping force, so the 
object's displacement will increase forever. The slow frequency represents the 
increase in displacement and the fast frequency represents the displacement itself.

The difference between the analytical and numerical solutions starts out small, but
as t>>0, it begins to increase more and more.

"""
