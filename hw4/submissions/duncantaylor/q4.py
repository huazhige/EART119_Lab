#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:31:29 2019

@author: taylorduncan
"""
import math

def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = float(f_x1 - f_x0)/(x1 - x0)
            x = x1 - float(f_x1)/denominator
        except ZeroDivisionError:
            return "Error! - denominator zero"
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps:
        iteration_counter = -1
    return x, iteration_counter
    

def f1(x):
    return -x**5+(1/3)*x**2+(1/2)

def f2(x):
    return (math.cos(math.radians(x)))**2+0.1

def f3(x):
    return math.sin(math.radians(x/3)) + 0.1*(x+5)


#Answers printed here
print(secant(f1, -10, 10, 0.001))

print(secant(f2, -10, 10, 0.001))

print(secant(f3, -3, 3, 0.001))

