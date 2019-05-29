import numpy as np

def function(x):
             # -10 < x < 10
    return(-(x**5) + (1./3.)*(x**2) + 0.5 )

def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken
 
f = lambda x: -(x**5) + (1./3.)*(x**2) + 0.5
 
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
 
f = lambda x: (np.cos(x))**2 + 0.1
 
root, steps = secant_method(f, 0, 10)
print ("root is:", root)
print ("steps taken:", steps)
print ("There is no root")



def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken
 
f = lambda x: np.sin(x/3) + 0.1*(x + 5)
 
root, steps = secant_method(f, -3, 3)
print ("root is:", root)
print ("steps taken:", steps)

