
import numpy as np
import matplotlib.pyplot as plt


#===================================================================================
#                          defining functions
#===================================================================================

def f(x):
    return(-(x**5) + (2/5)*(x**2) - 2)
def g(x):
    return(np.exp(-x/10) + x)
def h(x):
    return(10* np.sin(x/3) + 0.1*(x + 12))
#===================================================================================
#                          secant method for 3 functions
#===================================================================================

def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):#secant method and itteration 
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken
 
f = lambda x: -(x**5) + (2/5)*(x**2) - 2
 
root, steps = secant_method(f, 2, 8)
print ("root is:", root)
print ("steps taken:", steps)


def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken
 
f = lambda x: np.exp(-x/10) + x
 
root, steps = secant_method(f, 0, 10)
print ("root is:", root)
print ("steps taken:", steps)



def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken
 
f = lambda x: 10* np.sin(x/3) + 0.1*(x + 12)
 
root, steps = secant_method(f, -3, 3)
print ("root is:", root)
print ("steps taken:", steps)


#===================================================================================
#                          plotting
#===================================================================================

x0s = np.linspace(-10, 10, 5000) #assigning another varible to plot
for x0 in x0s:
    secant_method(x, x0, x1, max_iter=100, tolerance = 1e-5)



plt.plot(x0s, f(t))
plt.plot(x0s, g(t))
plt.plot(x0s, h(t))
plt.title('Crossover points of f(x1), f(x2), f(x3)')
plt.show()
#plt.savefig





