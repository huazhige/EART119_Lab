# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:06:33 2019
Homework 6
@author: Benny Quiroz
"""

"""
Questions 1 and 2 mixed together.
"""
import numpy as np
import matplotlib.pyplot as plt
import ODE_utils as odu

#------------------------------------------------------------------------------
#    Given Values et al.
#------------------------------------------------------------------------------

w = (2*np.pi)/(24*3600)
#I am using B for the alpha value, sorry.
B = 0.00001
#This is to make writing the exact function and its derivative easier and cleaner.
C = -1*np.sqrt(w/(2*B))
#The fluctuation in degrees.
fluc = 50.
#The depth at which we are modeling.
L = 4.
#Breaking up our depth into 40 intervals
x = np.linspace(0, L, 41)
#Defining the space between each interval
dx = x[1] - x[0]

#------------------------------------------------------------------------------
#    Functions
#      Needed to find the numerical derivative at all 41 depths.
#------------------------------------------------------------------------------

#Exact function for plotting later
def exact(x, t):
    return fluc*np.exp(x*C)*np.cos(x*C + w*t)

#Derivative of the exact function, needed in derivative computation at the end point.
#I know technically I needed to know the solution first in order to find this.  
#However, if we assume that the temperature is constant at a depth of 4 meters (foreshadowing)
#we can replace this with zero and the answer does not change.
def dudx(x, t):
    return fluc*C*np.exp(C*x)*(np.cos(x*C - w*t) - np.sin(x*C + w*t))

#Function for the temperature at the surface as a function of time. 
def s(t):
    return fluc*np.cos(w*t)

#The derivative of above, needed for the derivative function.
def dsdt(t):
    return -fluc*w*np.sin(w*t)

#Assuming no internal temperature changes.
def g(x, t):
    return 0 

#The big bad function that computes the derivative at each depth which will be used
#for the ode solving function. This is implemented from the book but I understand
#the math behind it.
def rhs(u, t):
    N = len(u) - 1
    rhs = np.zeros(N + 1)
    rhs[0] = dsdt(t)
    for i in range(1, N):
        rhs[i] = (B/dx**2)*(u[i + 1] - 2*u[i] + u[i - 1]) + g(x[i], t)
    rhs[N] = (B/dx**2)*(2*u[N - 1] + 2*dx*dudx(L, t) - 2*u[N]) + g(x[N], t)
    return rhs

#------------------------------------------------------------------------------
# Plots
#------------------------------------------------------------------------------

"""
We need starting conditions for our ode solver. Since we don't know the temperatures
at each depth without the exact solution we have to just let them all equal zero.
Except of course for the surface.
Starting at internal temperatures of zero will render our simulation inaccurate, 
however, since Mars has been heating and cooling well before our simulation has 
started. 
We can fix this by letting the teperatures begin at the average and then letting them 
acclimate to the changing temperature for a full temp cycle (one day). 
Then we can use the second day as the model against our exact solution.
"""
U0 = np.zeros(41)
U0[0] = s(0)

plt.figure(1)
"""
So this is a time step of 60 seconds over a period of 2 days.
This will give us a set of temperatures at each depth for each time step.
We can plot them in an animation or something but for our purposes we can just
plot a few throughout the day. 

The other thing that I should adress is why I am only doing this over the time 
period of one day as opposed to 10 mentioned in the problem.
The reason is that the temperature is cyclical over one day and looking at 
more than on will not change anything. Also much easier to plot.
"""
u0, t0 = odu.ode_FE(rhs, U0, 60, 24*3600*2)
"""
This is where it gets a bit tricky. I want to divide the second day up into 4 time
intervals with the 5th being the end of the day and return to the starting temperatures.
Our time bin is 2 days long though. 
To fix this you just have to do some fractions showing that 1/2 + 3/4 = 7/8 for example. 
"""
y00 = u0[int(len(u0)/2), :]
y01 = u0[int(5*len(u0)/8), :]
y02 = u0[int(3*len(u0)/4), :]
y03 = u0[int(7*len(u0)/8), :]
y04 = u0[len(u0) - 1, :]

#Plotting each time on a different subplot. Only added legend and title to first
#one for cleanliness.
plt.subplot(231)
plt.plot(x, y00, 'k-', alpha = 0.5, label = 'Approximation at dt of one minute')
time0 = t0[int(len(u0)/2)]/3600
plt.plot(x, exact(x, time0*3600), 'r-', alpha = 0.5, label = 'Exact')
plt.title('Temp as a function of depth (m) @ t = %.1f hours'%time0)
plt.legend()

plt.subplot(232)
plt.plot(x, y01, 'k-', alpha = 0.5)
time1 = t0[int(5*len(u0)/8)]/3600
plt.plot(x, exact(x, time1*3600), 'r-', alpha = 0.5)
plt.title('t = %.1f hours'%time1)

plt.subplot(233)
plt.plot(x, y02, 'k-', alpha = 0.5)
time2 = t0[int(3*len(u0)/4)]/3600
plt.plot(x, exact(x, time2*3600), 'r-', alpha = 0.5)
plt.title('t = %.1f hours'%time2)

plt.subplot(234)
plt.plot(x, y03, 'k-', alpha = 0.5)
time3 = t0[int(7*len(u0)/8)]/3600
plt.plot(x, exact(x, time3*3600), 'r-', alpha = 0.5)
plt.title('t = %.1f hours'%time3)

plt.subplot(235)
plt.plot(x, y04, 'k-', alpha = 0.5)
time4 = t0[len(u0) - 1]/3600
plt.plot(x, exact(x, time4*3600), 'r-',alpha = 0.5)
plt.title('t = %.1f hours'%time4)

#------------------------------------------------------------------------------
#   Plots continued.
#------------------------------------------------------------------------------

#This is just like Figure one except all of the time steps are plotted on the same
#graph. This allows us to look at the fluctuations over time. 
plt.figure(2)
u0, t0 = odu.ode_FE(rhs, U0, 60, 24*3600*2)
y00 = u0[int(len(u0)/2), :]
y01 = u0[int(5*len(u0)/8), :]
y02 = u0[int(3*len(u0)/4), :]
y03 = u0[int(7*len(u0)/8), :]
y04 = u0[len(u0) - 1, :]

plt.plot(x, y00, 'k-', alpha = 0.5)
time0 = t0[int(len(u0)/2)]/3600
plt.plot(x, exact(x, time0*3600), 'r-', alpha = 0.5)

plt.plot(x, y01, 'k-', alpha = 0.5)
time1 = t0[int(5*len(u0)/8)]/3600
plt.plot(x, exact(x, time1*3600), 'r-', alpha = 0.5)

plt.plot(x, y02, 'k-', alpha = 0.5)
time2 = t0[int(3*len(u0)/4)]/3600
plt.plot(x, exact(x, time2*3600), 'r-', alpha = 0.5)

plt.plot(x, y03, 'k-', alpha = 0.5)
time3 = t0[int(7*len(u0)/8)]/3600
plt.plot(x, exact(x, time3*3600), 'r-', alpha = 0.5)

plt.plot(x, y04, 'k-', alpha = 0.5)
time4 = t0[len(u0) - 1]/3600
plt.plot(x, exact(x, time4*3600), 'r-',alpha = 0.5)

#Graphhing the lines y = 1 and y = -1 so that we can see when the fluctuations
#are between them. 
one = np.ones(len(x))
plt.plot(x, one, x, -1*one, 'g-')
#Zooming in on the relevant region.
plt.xlim(1, 3)
plt.ylim(-3, 3)
plt.title('Fluctuations in tempature over time against depth(m)')

"""
Looking at Figure 2, the depth at which the temperature fluctuations are within
+/- 1degC is at a depth of about 2 meters. I would recommend that Tintin dig
about that deep. 
"""

#------------------------------------------------------------------------------
#   Plots continued.
#------------------------------------------------------------------------------

"""
For this one, it's just the same as Figure 1 except that I have changed the time 
step to one that is larger. I had to search around for a time step that showed
the instability of the approximation without losing too much context in the figures.
That's why the time step is so weird.  
"""
plt.figure(3)
u1, t1 = odu.ode_FE(rhs, U0, 60*8.4, 24*3600*2)
y10 = u1[int(len(u1)/2), :]
y11 = u1[int(5*len(u1)/8), :]
y12 = u1[int(3*len(u1)/4), :]
y13 = u1[int(7*len(u1)/8), :]
y14 = u1[len(u1) - 1, :]

plt.subplot(231)
plt.plot(x, y10, 'k-', label = 'Approximation at dt of 8.4 minutes, unstable')
time10 = t1[int(len(u1)/2)]/3600
plt.plot(x, exact(x, time10*3600), 'r-', label = 'Exact')
plt.title('Temp as a function of depth (m) @ t = %.0f hours'%time10)
plt.legend()

plt.subplot(232)
plt.plot(x, y11, 'k-')
time11 = t1[int(5*len(u1)/8)]/3600
plt.plot(x, exact(x, time11*3600), 'r-', label = 't = %.1f hours'%time11)
plt.title('t = %.0f hours'%time11)

plt.subplot(233)
plt.plot(x, y12, 'k-')
time12 = t1[int(3*len(u1)/4)]/3600
plt.plot(x, exact(x, time12*3600), 'r-', label = 't = %.1f hours'%time12)
plt.title('t = %.0f hours'%time12)

plt.subplot(234)
plt.plot(x, y13, 'k-')
time13 = t1[int(7*len(u1)/8)]/3600
plt.plot(x, exact(x, time13*3600), 'r-', label = 't = %.1f hours'%time13)
plt.title('t = %.0f hours'%time13)

plt.subplot(235)
plt.plot(x, y14, 'k-')
time14 = t1[len(u1) - 1]/3600
plt.plot(x, exact(x, time14*3600), 'r-', label = 't = %.1f hours'%time14)
plt.title('t = %.0f hours'%time14)

#------------------------------------------------------------------------------
#   Plots continued.
#------------------------------------------------------------------------------

"""
This last figure shows what the approximation looks like when it is wildly unstable. 
I used a time step of 10 minutes. 
"""

plt.figure(4)
u1, t1 = odu.ode_FE(rhs, U0, 60*10, 24*3600*2)
y10 = u1[int(len(u1)/2), :]
y11 = u1[int(5*len(u1)/8), :]
y12 = u1[int(3*len(u1)/4), :]
y13 = u1[int(7*len(u1)/8), :]
y14 = u1[len(u1) - 1, :]

plt.subplot(231)
plt.plot(x, y10, 'k-', label = 'Approximation at dt of 10 minutes, wildly unstable')
time10 = t1[int(len(u1)/2)]/3600
plt.plot(x, exact(x, time10*3600), 'r-', label = 'Exact')
plt.title('Temp as a function of depth (m) @ t = %.0f hours'%time10)
plt.legend()

plt.subplot(232)
plt.plot(x, y11, 'k-')
time11 = t1[int(5*len(u1)/8)]/3600
plt.plot(x, exact(x, time11*3600), 'r-', label = 't = %.1f hours'%time11)
plt.title('t = %.0f hours'%time11)

plt.subplot(233)
plt.plot(x, y12, 'k-')
time12 = t1[int(3*len(u1)/4)]/3600
plt.plot(x, exact(x, time12*3600), 'r-', label = 't = %.1f hours'%time12)
plt.title('t = %.0f hours'%time12)

plt.subplot(234)
plt.plot(x, y13, 'k-')
time13 = t1[int(7*len(u1)/8)]/3600
plt.plot(x, exact(x, time13*3600), 'r-', label = 't = %.1f hours'%time13)
plt.title('t = %.0f hours'%time13)

plt.subplot(235)
plt.plot(x, y14, 'k-')
time14 = t1[len(u1) - 1]/3600
plt.plot(x, exact(x, time14*3600), 'r-', label = 't = %.1f hours'%time14)
plt.title('t = %.0f hours'%time14)

"""
Question 3
By playing around the the max temperature, e.g. changing it to +/- 80, I was able 
to see that the depth at which the fluctations die down does not change. 

"""
