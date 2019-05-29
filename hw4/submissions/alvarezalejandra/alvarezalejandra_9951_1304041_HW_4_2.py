import numpy as np
import matplotlib.pyplot as plt

#some constants
A = 5
c = 1.1
t_0 = 2.5

#=========================================================================
#                         defining all functions
#=========================================================================
def f(t):
    return c*(t - t_0)**2

def g(t):
    return A*t + t_0

def h(t):
    return f(t) - g(t)

def dfdt(t):
    return 2*c*(t - t_0)

def dgdt(t):
    return A

def dhdt(t):
    return 2*c*(t - t_0)- A

def dh(f, t):
    return abs(0 - f(t))
#=========================================================================


roots = []
def newton_method(h, dh, x0, tol): 
    delta = dh(h , x0)
    while delta > tol: #tol (tolerance) is the same as epsilon
        x0 = x0 - h(x0)/dhdt(x0)
        delta = dh(h , x0)
        #print(delta)
    #print ('Root is at: ', x0)
    #print ('f(x) at root is: ', f(x0))
    if round(x0, 3) not in roots: #rounding numbers to make it easier to work with
        roots.append(round(x0, 3))

    
x0s = np.linspace(-10, 10, 500) #calling function
for x0 in x0s:
    newton_method(h, dh, x0, 1e-5)

roots = np.asarray(roots)
froots = f(roots)

print(roots)
print(froots)


plt.plot(x0s, g(x0s))
plt.plot(x0s, f(x0s))
plt.title('Crossover points of f(t)-g(t)')
plt.show()
#plt.savefig("HW_4_2.png", bbox_inches='tight')


"""
2c) in 2_1_fct_cross_over.py, the crossover point is >0 but in HW_4_2 the crossover point is <0.

"""


