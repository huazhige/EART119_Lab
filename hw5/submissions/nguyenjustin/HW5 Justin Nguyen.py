# =============================================================================
# Python 2, Anaconda 2.7
# Justin Nguyen
# EART 119
# =============================================================================
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
def solution_euler(time, Parr):
    nSteps    = time.shape[0]
    au_hat    = np.zeros( nSteps)
    au_hat[0] = Parr['y0']
    av_hat    = np.zeros( time.shape[0])
    av_hat[0] = Parr['y1']
    for i in range( nSteps-1):
        # slope at previous time step, i (these are the right hand sides of the ODEs)
        fn_1 = av_hat[i]
        fn_2 = Parr['F']*np.cos(Parr['w']*time[i]) - Parr['w0']**2*au_hat[i]
        # euler formula: y[n+1] = y[n] + fn*h
        au_hat[i+1] = au_hat[i] + fn_1 * Parr['h'] 
        av_hat[i+1] = av_hat[i] + fn_2 * Parr['h']

    return au_hat, av_hat

#analytic solution for w = w0
def solution_phase_ana(time, Parr):
    return Parr['F']/(Parr['w0']*2) * time * np.sin(Parr['w0']*time)
    
# =============================================================================
# Plotting and Calculations
# =============================================================================
#analitic solution w =! w0
au_hat, av_hat = solution_euler(time, Parr)

#analitic solution w = w0
phase_au_hat, phase_av_hat = solution_euler(time, phaseParr)

#plotting for the first part
plt.figure(1)
plt.plot(time, 3*np.sin(0.1*time), 'k--')
plt.plot(time, sol_an(time, Parr), 'g-') #plotting analytic solution
plt.plot(time, Force(time, Parr), 'b-', linestyle = 'solid', alpha = 0.5) #plotting forcing function
plt.plot(time, au_hat, 'r-')
plt.plot(time, -3*np.sin(0.1*time), 'k--')
plt.legend(["Analystic Solution Full Slow","Analytic Solution","Forcing Function","Euler's Method"])
plt.ylabel('y(t)')
plt.xlabel("Time(t)")
plt.savefig('problem 1 figure')
plt.show()

#plotting for the 2nd part
plt.figure(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(time, phase_au_hat, 'g-')
ax1.plot(time, solution_phase_ana(time, phaseParr), 'b-')
ax1.legend(["Analytic Solution", "Euler's Method"], loc = 'bottom left')
ax1.set_ylabel('y(t)')
ax2.plot(time, solution_phase_ana(time, phaseParr) - phase_au_hat, 'r-')
ax2.set_ylabel('Numerical Solution')
ax2.set_xlabel('Time')
ax2.legend(["Analytic Solution"], loc = 'bottom left')
plt.savefig('problem 2 figure')
plt.show()
