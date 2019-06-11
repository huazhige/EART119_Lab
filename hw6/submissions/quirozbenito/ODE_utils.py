# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:45:29 2019

@author: Benny Quiroz
"""
import numpy as np
import matplotlib.pyplot as plt


"""
f is a growth rate function
U_0 is an initial value
dt is the time step for estimation
T is the total time window
"""
def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    f_ = lambda u, t: np.asarray(f(u, t))
    u = np.zeros((N_t + 1, len(U_0)))
    t = np.linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n + 1] = u[n] + dt*f_(u[n], t[n])
    return u, t

def demo_population_growth():
    def f(u, t):
        return 0.1*(1-u/500)*u
    
    u, t = ode_FE(f, 100, 0.5, 60)
    plt.plot(t, u)
    plt.show()
    
#demo_population_growth()
    
def demo_SIRV():
    def f(u, t):
        S, I, R = u
        return [-b*S*I, b*S*I - g*I, g*I]
    
    b = 3./(40*8*24)
    g = 3./(15*24)
    u, t = ode_FE(f, [50, 1, 0], 0.1 ,30*24)
    S = u[:, 0]
    I = u[:, 1]
    R = u[:, 2]
    p1,p2, p3 = plt.plot(t, S, t, I, t, R)
    plt.plot()
    
#demo_SIRV()
    

