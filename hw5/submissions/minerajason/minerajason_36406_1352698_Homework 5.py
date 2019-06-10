# -*- coding: utf-8 -*-
"""
@author: Jason

consider the initial value problem:
    m*y''+ k*y = F*cos(omega*t)
with the IC y(0) = y'(0) = 0, for m =1, we can rewrite the 
equations as:
    y'' + omega**2 * y = F*cos(omega * t)
where omega naught = (K/m)^0.5 is the natural frequency of
the oscillating system

a.)Exact solution general frorm 
   y = c1 * cos(w0*t) + c2 * sin(w0*t) + [F/(w0**2 - w**2)]*cos(w*t)
   
b.)y(0)  = 0 = c1*1 + 0 + [F/((w0**2 - w**2))*1]
    
        c1 = -F/(w0**2 - w**2)

   y'(0) = 0 = 0 + c2*w0*1 - 0 
   
        c2 = 0

c.)
    y = c1 * cos(w0*t) + [F/(w0**2 - w**2)]*cos(w*t)
    
    in part b we proved c1 = -F/(w0**2 - w**2)
    
    y = c1 * cos(w0*t) + [-c1]*cos(w*t)
    
    a difference of cosine can be written as [-2 * sin((w0+w)/2)*t)*sin((w0-w)/2)*t]
 
    
g.) when the frequencies are in phase the amplitude increases.
"""
import numpy as np
import matplotlib.pyplot as plt

#################################Parameters####################################

Para ={'F': 0.5,
       'w_0':0.8,
        'w': 1.,
        'Start_T': 0,
        'End_T': 94,
        'delta': 1e-3,
        'y0': 0,
        'y1': 0
       }


time = np.arange(Para['Start_T'], Para['End_T'], Para['delta'])

def analytic(time, Para):
    return Para['F']/((Para['w_0']**2 - Para['w']**2)) * (2 * np.sin(time*[Para['w_0'] + Para['w']]/2) * np.sin(time*[Para['w_0'] - Para['w']]/2))

def force(time, Para):
    return Para['F']*np.cos(Para['w'] * time)

def euler(time, Para):
    
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
    numSt = time.shape[0]
    au_hat = np.zeros(numSt)
    au_hat[0] = Para['y0']
    av_hat = np.zeros(time.shape[0])
    av_hat[0] = Para['y1']
    for i in range (numSt - 1):
        fn1 = av_hat[i]
        fn2 = Para['F']*np.cos(Para['w']*time[i]) - Para['w_0']**2*au_hat[i]
        
        au_hat[i+1] = au_hat[i] + fn1 * Para['delta']
        av_hat[i+1] = av_hat[i] + fn2 * Para['delta']
        
    return au_hat, av_hat
    
phPara = {'F': 0.5,
        'w': 1.,
        'w_0':1.,
        'tstart': 0,
        'tend': 94,
        'delta': 1e-3,
        'y0': 0,
        'y1': 0
        }
def phase_analytic(time,Para):
    return Para['F']/(Para['w_0']*2)*time*np.sin(Para['w_0']*time)



au_hat, av_hat = euler(time, Para)


phase_au_hat, phase_av_hat = euler(time, phPara)

#first plot
plt.figure(1)
plt.plot(time, analytic(time, Para), 'yellow') 
plt.plot(time, force(time, Para), 'black', linestyle = 'solid', alpha = 0.5) 
plt.plot(time, analytic(time, Para), '--', color = '0.5', lw = 2, label = 'ana - env')
plt.plot(time, analytic(time, Para), '--', color = '0.5', lw = 2, label = 'ana - env')
plt.plot(time, au_hat, 'y')
plt.legend(["Forcing Function","Analytic Solution","Euler's Method"])
plt.ylabel('Disp [mm]')
plt.xlabel("Time [s]")
plt.show()


#Second plot
plt.figure(2)
ax1 = plt.subplot(211)
ax1.plot(time, phase_analytic(time, phPara), 'b-')
ax1.plot(time, phase_au_hat, 'g-')
ax1.legend(["Analytic Solution", "Euler's Method"], loc = 'upper left')
ax1.set_ylabel('y(t)')

ax2 = plt.subplot(212)
ax2.plot(time, phase_analytic(time, phPara) - phase_au_hat)
ax2.set_ylabel('Disp [mm]')
ax2.set_xlabel('Time [s]')
plt.show()
