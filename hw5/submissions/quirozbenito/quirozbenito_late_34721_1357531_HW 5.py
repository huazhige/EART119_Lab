# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:45:46 2019
Homework 5 
@author: Benny Quiroz
"""

import numpy as np
import matplotlib.pyplot as plt
import modules.ODE_utils as odu

"""
a, b, c)
y = c1cos(w0t) + c2sin(w0t) + [F/(w0^2 - w^2)]cos(wt)
For y(0) = 0:
0 = c1 + 0 + F/(w0^2 - w^2)
c1 = - F/(w0^2 - w^2)

y' = ~~~sin(w0t) = c2w0cos(w0t) - ~~~sint(wt)
where ~~~ is constants
For y'(0) = 0:
0 = 0 + c2w0 - 0
c2 = 0

So the original function becomes:
y = [F/(w0^2 - w^2)]*(cos(wt) - cos(w0t))
y = [-2F/(w0^2 - w^2)]*(sin((wt + w0t))/2)*sin((wt - w0t)/2)
This is what we're going to plot below. 
"""
#All of our given information
F = 0.5
w0 = 0.8
w = 1
A = -F/(w0**2 - w**2)

#This is the exact solution
def f_AnaSolution(t):
    return 2*A*np.sin((w*t + w0*t)/2)*np.sin((w*t - w0*t)/2)
#an array of times that can be used to discretize our exact functions
t = np.linspace(0, 100, 1001)

#This is just the forcing function
def f_Forcing(t):
    return F*np.cos(w*t)

"""
For the function that gives the derivatives, we have to analyze the general equation
for these systems. 
u'' = F*np.cos(w*t) - u*(w0**2)
This can be broken into two equations that can be coded:
u' = v
v' = F*np.cos(w*t) - u*(w0**2)
"""
def f_FE(u, t):
    u, v = u
    return [v, F*np.cos(w*t) - u*(w0**2)]

#This is finding the points for the Forward Euler approximation
u, t1 = odu.ode_FE(f_FE, [0,0], 0.01, 100)

#Plot of the analytic solution and it's component equations.
plt.subplot(221)
plt.cla()
plt.plot(t, f_AnaSolution(t), 'k-', label = 'analytic solution')
plt.plot(t, 2*A*np.sin((w*t + w0*t)/2), 'g-', alpha = 0.5, label = 'fast frequency')
plt.plot(t, 2*A*np.sin((w*t - w0*t)/2), 'b-', alpha = 0.5, label = 'slow frequency')
plt.title('I. - III. Beats')
plt.legend(prop={'size': 8})

#Adding in the forcing function
plt.subplot(222)
plt.plot(t, f_AnaSolution(t), 'k-', label = 'analytic solution')
plt.plot(t, f_Forcing(t), 'r-', label = 'Forcing frequecy')
plt.legend()

#This is the Euler approximation.
plt.subplot(223)
#The first column of u is the position approximations which is what we want.
#The second is the velocity approzimations.
plt.plot(t1, u[:,0], 'r-', alpha = 0.5, label = 'Forward Euler')
plt.plot(t, f_AnaSolution(t), 'k-', label = 'analytic solution')
plt.legend()

plt.show()

"""
f.)c.)
Time steps around 1e-3 are very accuate for the first 3 periods. 
The graph shown in the plot uses a time step of 1e-2 which is still very accurate
for the first period.
"""

"""
Problem 2

If the forcing frequency and oscillating frequency are the same, the oscillations
begin to grow very large in amplitude.

Taking a look at the new function as before. 
y = c1cos(wt) + c2sin(wt) + (F/2w)tsin(wt)
For y(0) = 0 
0 = c1 + 0 + 0
c1 = 0
For y'(0) = 0
y' = ~~~sint(wt) + c2cos(wt) + (f/2w)*(wtcos(wt) + sin(wt))
0 = 0 + c2 + 0
c2 = o
So the equation becomes:
y = (F/2w)(tsin(wt))
which we can plot below.
"""

#This is theanalytic solution for Problem 2
def f_Ana1Solution(t):
    return (F/(2*w))*t*np.sin(w*t)

#This is so I could test which column of u I should use.
#If we plot the other one, it'll line up with the plot of the solutions derivatve.
    
#def Ana1Deriv(t):
#    return (F/(2*w))*(w*t*np.cos(w*t) + np.sin(w*t))

#The derivative as a function of time and position. Found just like we did above.
def f_FE1(u, t):
    u, v = u
    return [v, F*np.cos(w*t) - u*(w**2)]

u1, t2 = odu.ode_FE(f_FE1, [0,0], 0.01, 100)
plt.subplot(224)
plt.plot(t2, u1[:,0], 'r-', alpha = 0.5, label = 'Forward Euler')
plt.plot(t, f_Ana1Solution(t), 'k-', label = 'Analytic Solution')
plt.title('IV. Natural Frequency')
plt.legend()
#plt.plot(t, Ana1Deriv(t), 'b-', alpha = 0.5)
plt.show()

"""
2.)j.)
I don't think that Hooke's law is particularly applicable to this part just because
of all the terms we added to the equation. However the quation does imply that 
y ~ F but I'm not sure how the sin term interacts. In real life, I think the oscillator
would go to it's maximum reasonable amplitude very quickly.

This one, like before was very accurate for the time step ~ 10e-2 in the first few
periods. I graphed it like this to be the same as the other plots. If we decrease the 
time step, the approximation becomes near perfect.

"""