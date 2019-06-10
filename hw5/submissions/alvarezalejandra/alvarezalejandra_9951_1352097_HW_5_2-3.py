import numpy as np
import matplotlib.pyplot as plt


def dfdx(x, f):
    return (0.5 / 2 * 0.8) * x * np.sin(0.8 * x)

#def f_int(x, C):
#    return 0.3125 * (-1.25 * x * np.cos(0.8 * x) + 1.5625 * np.sin(0.8 * x)) + C
#defined this as the integral but realized it should be derivative

def f_int(x, C):
    return (0.25*0.8*x*np.sin(0.8*x) + 0.8*x*np.cos(0.8*x))

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

def func2(x):
    return (0.5 / 2 * 0.8) * x * np.sin(0.8 * x)

def func2(x):
    return (0.5 / 2 * 0.8) * x * np.sin(0.8 * x)

def integrallama(x, C):
    return 0.3125 * (-1.25 * x * np.cos(0.8 * x) + 1.5625 * np.sin(0.8 * x)) + C

N = 100
x_anal = np.linspace(0, 10 , N)
y = func2(x_anal)
#plt.plot(x_anal, y, label = 'Analytical')


a = 0.0
b = 10.0
f_a = 0.0
N = 100
#x_2, f_2 = euler_wrapper(dfdx, a, b, f_a, N)
x_4, f_4 = rk4(dfdx, a, b, f_a, N)
#x = x_2.copy()

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax2 = fig.add_subplot(211)

ax1.plot(x_4,f_4)
ax2.plot(x_anal, y, label = 'Analytic')
plt.legend(frameon = False)
#plt.plot(x, f_int(x, f_a), "o", label = "Analytic")

'''
this part of the problem shows omega being equal to omega not and their graphs are similar but 
in reality this is not possible or you could say that object is not being displaced.
'''