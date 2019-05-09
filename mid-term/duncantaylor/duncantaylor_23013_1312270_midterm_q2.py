import math
import matplotlib.pyplot as plt

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
    return x**5+(2/5)*x**2-2

def f2(x):
    return (math.exp(-x/10))+x

def f3(x):
    return math.sin(math.radians(x/4))+ 0.1*(x+12)


#Answers printed here
print(secant(f1, -10, 10, 0.001))

print(secant(f2, -10, 10, 0.001))

print(secant(f3, -10, 10, 0.001))
 
#plotting

plt.subplot(311)
ax1= plt.subplot(311)
ax2= plt.subplot(312)
ax3= plt.subplot(313)
plt.show()

#ANSWERS BELOW
"""
#Error! - denominator zero for f1
#(-1.118200337740603, 3)   for f2
#(-11.498818261138197, 2)  for f3

"""
# -*- coding: utf-8 -*-

