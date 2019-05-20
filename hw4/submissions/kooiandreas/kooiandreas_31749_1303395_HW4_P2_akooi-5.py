#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
NOTE: I did edit opt_utils and the 2_1 file a bit, so I attached them alongside with the homework.

Created on Sun May  5 11:39:14 2019

@author: andreaskooi


Find the intersection (cross-over point) between the following two functions using
Newton’s or the Secant method (Hint: solve for 𝑓(𝑡) − 𝑔(𝑡) = 0)!
• 𝑓(𝑡) = 𝑐(𝑡 − 𝑡*)+, with t0 = 2.5, c = 1.1, and −10 ≤ t ≤ 10
• 𝑔(𝑡) = 𝐴𝑡 + 𝑡*, with A = 5, and −10 ≤ t ≤ 10
a) How many cross-over points are there for −10 ≤ t ≤ 10?
b) What are the values of t, 𝑓(𝑡) and 𝑔(𝑡)?
c) Compare your solutions with the solution from week 2 (in class assignment
inC_2_1_vec_matrix.pdf, functions and vectors). For the comparison:
plot 𝑓(𝑡) − 𝑔(𝑡) and one of the cross-over points detected with both methods.
You may have to zoom a bit to see the difference. Save the plot as .png and
submit to canvas.


"""

#=============================================================================
#       imports and functions
#=============================================================================

import method_2_1 as fco
import opt_utils as ou
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 1.1*(t - 2.5)**2

def g(t):
    return 5*t + 2.5

def f_minus_g(t):
    return (1.1*(t - 2.5)**2) - (5*t + 2.5)

def f_minus_g_dt(t):
    return 2.2*(t - 2.5) - 5


#=============================================================================
            #calculations
#=============================================================================

# from drawing f(t) and g(t) on paper, I expect two intersections, one at around
# 1 and the other at around 9. This is also expected since f(t) is a downward
# parabola and g(t) is positive linear

intersect_1 = ou.my_Newton(f_minus_g, f_minus_g_dt ,1)
intersect_2 = ou.my_Newton(f_minus_g, f_minus_g_dt ,9)


#=============================================================================
#           printing and plotting answers for parts a - c
#=============================================================================

print("NOTE: I did edit opt_utils and the 2_1 file a bit, so I attached them alongside with the homework.")

print("answers:")
print("a.)")
print("there are two intersections")
print("b.)")
print('intersection times, t: ', intersect_1, 'and ', intersect_2)
print('values of f(t) at these times:', f(intersect_1), 'and ', f(intersect_2))
print('values of g(t) at these times:', g(intersect_1), 'and ', g(intersect_2))
print("c.)")
    
'''
numerical answers (without printing):
('intersection times, t: ', 0.43663998885219746, 'and ', 9.108814777994459)
('values of f(t) at these times:', 4.683199989164247, 'and ', 48.04407604682174)
('values of g(t) at these times:', 4.683199944260988, 'and ', 48.044073889972296)
'''

result_2_1 = fco.main()
intersect_2_1 = result_2_1[0]
t = np.linspace(-3,3,15)
plt.figure()
plt.plot(t, f(t), 'r-', label = 'f(t)')
plt.plot(t, g(t), 'b-', label = 'g(t)')

plt.plot(intersect_1, f(intersect_1), 'y*', label='Intersection using Newtons method')
plt.plot(intersect_2_1, f(intersect_1), 'g*', label = 'Intersection using IC_2_1 method')

plt.legend()

plt.title("HW4_P2_fig")
plt.xlabel("t")
plt.ylabel("f(t) and g(t)")
plt.plot()

plt.savefig('HW4_P2_figure')





    