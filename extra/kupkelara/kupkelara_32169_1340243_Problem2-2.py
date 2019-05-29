#! python3
"""Compute the mean and integral of the function over the given domain"""
import numpy as np

def integrate_and_mean(function, minimum, maximum, sampling):
    vec = np.linspace(minimum, maximum, sampling)
    value = function(vec)
    delta = vec[1] - vec[0]
    
    #integrate
    summation_trap = 0
    for i in range(accuracy):
        summation_trap = value[i] + value[i-1] +summation_trap
    solution_trap = delta_t/2 * summation_trap

    summation_rect = 0
    for i in range(accuracy-1):
        summation_rect = value[i]*delta_t +summation_rect
        
    mean = np.mean(value)
    
    return solution_trap, summation_rect, mean

#functions
f = lambda x: np.sin(x)
g = lambda x: 2*x*np.e**x**2

N = 1000

f_solution = integrate_and_mean(f, 0, np.pi, N)
print('f integral:', f_solution[0], 'f mean:', f_solution[2] )

g_solution = integrate_and_mean(g, 0, 1, N)
print('g integral:', g_solution[0], 'g mean:', g_solution[2] )
