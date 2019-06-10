import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 2.78*(np.sin(0.9*x) * np.sin(0.1*x))

# def forcing_func(F, omega, omega_not):
#     return -F*((omega_not**2) - (omega**2))

def forcing_func(F, omega, t):
    return F * np.cos(omega * t)

N = 100
x_anal = np.linspace(0, 100 , N)
y = func(x_anal)
plt.plot(x_anal, y, label = 'Analytical')
y_forcing = forcing_func(0.5, 1, x_anal)
plt.plot(x_anal, y_forcing, label = 'Forcing')

def dfdx(x,f):
    return 2.78*(np.sin(0.9*x) * np.sin(0.1*x))

#def f_int(x,C):
#    return 2.78*(0.5*(-np.sin(x) + 1.25 * np.sin(0.8 * x)) + C)
#I set this up as an integral but realized it should be the derivative, did not want to change
# all of my code
def f_int(x, f):
	return 2.78*(np.cos(0.9*x)*0.9*np.sin(0.1*x) + np.cos(0.1*x)*0.1*np.sin(0.9*x))

def forward_euler(x_i, f_i, h , g):
    # advance f by a step h
    
    #half step
    x_ipoh = x_i + 0.5*h
    f_ipoh = f_i + 0.5*h*g(x_i, f_i)
    
    #full step
    f_ipo = f_i + h*g(x_ipoh, f_ipoh)
    
    return f_ipo

def euler_wrapper(dfdx, a, b, f_a, N):
    #dfdx is the derivative with respect to x
    #a is the lower bound
    #b is the upper bound
    #f_a is the boundary condition at a
    #N is the number of steps
    
    #define out steps
    x = np.linspace(a, b , N)
    
    #a single step size
    h = x[1] - x[0]
    
    #an array to hold f
    f = np.zeros(N, dtype = float)
    
    f[0] = f_a #value of f at a
    
    #evolve f along x
    for i in range(1, N):
        f[i] = forward_euler(x[i-1], f[i-1], h, dfdx)
        
    return x, f

def rk4_core(x_i, f_i, h, g):
    #define x at half step
    x_ipoh = x_i + 0.5 * h
    
    #define x at 1 step
    x_ipo = x_i + h
    
    #advance f by a step h
    
    k_1 = h * g(x_i, f_i)
    k_2 = h * g(x_ipoh, f_i + 0.5 * k_1)
    k_3 = h * g(x_ipoh, f_i + 0.5 * k_2)
    k_4 = h * g(x_ipo, f_i + k_3)
    
    f_ipo = f_i + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6.
    
    return f_ipo

def rk4(dfdx, a, b, f_a, N):
    #dfdx is the derivative with respect to x
    #a is the lower bound
    #b is the upper bound
    #f_a is the boundary condition at a
    #N is the number of steps
    
    #define out steps
    x = np.linspace(a, b , N)
    
    #a single step size
    h = x[1] - x[0]
    
    #an array to hold f
    f = np.zeros(N, dtype = float)
    
    f[0] = f_a #value of f at a
    
    #evolve f along x
    for i in range(1, N):
        f[i] = rk4_core(x[i-1], f[i-1], h, dfdx)
        
    return x, f


a = 0.0
b = 100.0
f_a = 0.0
N = 100
x_2, f_2 = euler_wrapper(dfdx, a, b, f_a, N)
x_4, f_4 = rk4(dfdx, a, b, f_a, N)
x = x_2.copy()


plt.plot(x_2, f_2, label = 'FE2')

plt.plot(x, f_int(x, f_a), "o", label = "Analytic")
plt.legend(frameon = False)
plt.title('Forward Euler')

plt.plot(x_4, f_4, label = 'RK4')
plt.plot(x, f_int(x, f_a), "o", label = "Analytic")

N = 100
x_anal = np.linspace(0, 100 , N)
y = func(x_anal)
plt.plot(x_anal, y, label = 'Analytical')
y_forcing = forcing_func(0.5, 1, x_anal)
plt.plot(x_anal, y_forcing, label = 'Forcing')
plt.legend(frameon = False)
plt.title('4th order runge kutta')


'''
As the difference between omega and omega not approach a small finite value 
they will be divded into the value F which will yield a large number. 
Since we are comparing three sinusoidal functions of near the same amplitude 
this division will yield a large output thus overpowering the output of the function.
'''

