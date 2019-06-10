"""
Lili Callahan 

Homework 5, Problem 1:
Solve second order, non-homogeneous ODE: Undamped harmonic oscillator
Compare analytical and numerical solutions

ODE: 
    my''(t) + gy'(t) + ky(t) = f(t)
    w0**2 = k/m

Analytical solution:
     y(t) = F/((w0**2 - w**2)*(cos(w*t) - cos(w0*t))

"""

import matplotlib.pyplot as plt
import numpy as np

###########################################################################
#       Dictionary and Parameters
###########################################################################

dPar = { # frequencies
         'w0'     : .8, # --> sqrt(k/m) --> natural frequency
         'w'      : 1,  # --> frequency of forcing function
         # forcing function amplitude
         'F'      : 0.5,
         # initial conditions for displ. and velocity
         'y01'    : 0, 'y02' : 0,
         # time stepping
         'h'      : 1e-2,
         'tStart' : 0,
         'tStop'  : 20*np.pi,}

###########################################################################
#       Analytical Solution: Parts a), b), and c) 
###########################################################################

# time variable
at        = np.arange(dPar['tStart'], dPar['tStop'] + dPar['h'], dPar['h'])

"""
Constants:
    c1 = -F/(w0**2 - w**2)
    c2 = 0
"""

# forcing function
fct_t     = dPar['F']*np.cos(dPar['w']*at)

# analytical solution as a product of sins
preFacAna = dPar['F']/(dPar['w0']**2 - dPar['w']**2)
ay_ana1   = preFacAna * (-2*np.sin((dPar['w']*at + dPar['w0']*at)/2)*np.sin((dPar['w']*at - dPar['w0']*at)/2))

# slow frequency
ay_ana2   = -2*preFacAna * (np.sin(((dPar['w'] - dPar['w0'])/2)*at))

###########################################################################
#       Numerical Solution: Part f)
###########################################################################

"""
This is part f) a. and I found the numerical solution to the ODE using the Forward Euler method.
I did not do parts f) b. or f) c. which were listed as bonus parts.
     
"""

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
    # set the initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step
        fn1 = av_hat[i]
        fn2 = -par['w']**2*au_hat[i] + dPar['F']*np.cos(dPar['w0']*i*dPar['h'])
        # euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn1*dPar['h']
        av_hat[i+1] = av_hat[i] + fn2*dPar['h']
    return au_hat, av_hat

aU_num, aV_num = num_sol(at, [dPar['y01'], dPar['y02']], dPar)

###########################################################################
#       Plotting: Parts d), e), and f)
###########################################################################

plt.figure(1)
ax = plt.subplot(111)
# analytical solution: fast frequency
ax.plot(at, ay_ana1, 'r--', lw = 1, label = 'ana - full')
# analytical solution: slow frequency
ax.plot(at, ay_ana2, '--', color = '.5', lw = 2, label = 'ana - env')
ax.plot(at, -ay_ana2, '--', color = '.5', lw = 2)
# forcing function
ax.plot(at, fct_t, 'b-', lw = 1, alpha = .5, label = 'forcing')
# numerical solution for comparison
ax.plot(at, aU_num, 'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Displacement [mm]')
ax.legend(loc = 'upper left')
plt.show()
plt.savefig('5.1_plot.png')

###########################################################################
#       Observations
###########################################################################

"""
Judging by the solution of y(t), it seems like the object, oscillating at w != w0, will 
continuously go back and forth between increasing in displacement and descreasing
in displacement. Since there is no damping force, the peak displacement is the same each period.
The slow frequency represents the increase and decrease in displacement, and the fast frequency 
represents the displacement itself.

"""

