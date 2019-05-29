#! python3
"""Compute the integral over the given domain using both midpoint
and trapazoidal methods
Answer: e-1 
"""

import numpy as np

#bounds
accuracy = 500

tmin = 0
tmax = 1

#function
f = lambda t: 3*(t**2)*np.e**(t**3)

#calculations
tvec = np.linspace(tmin, tmax,accuracy)
value = f(tvec)

delta_t = tvec[1]-tvec[0]

#trapazoid method
summation_trap = 0
for i in range(accuracy):
        summation_trap = value[i] + value[i-1] +summation_trap
solution_trap = delta_t/2 * summation_trap

#midpoint/rectangular method
summation_rect = 0
for i in range(accuracy-1):
    summation_rect = value[i]*delta_t +summation_rect

print('Trapazoidal integration:',solution_trap)
print('Midpoint integration:',summation_rect)
print('Real answer', np.e - 1)
