# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return -x**5+(0.33333)*x**2+(0.5)
    
def f2(x):
    return (np.cos(x))**2+0.1

def f3(x):
    return np.sin(x/3)+0.1*(x+5)

def secant(f, x0, x1, eps, xmin, xmax):
    f_x0 = f(x0)
    f_x1 = f(x1)
    x0 = float(x0)
    x1 = float(x1)
    iteration_counter = 0
    inInterval = True
    x = x0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = float(f_x1 - f_x0)/(x1 - x0)
            x = x1 - float(f_x1)/denominator
            if x < xmin or x>xmax:
                inInterval = False
        except ZeroDivisionError:
            print "Error! - denominator zero for x = ", x
#            sys.exit(1) # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps or inInterval==False:
        iteration_counter = -1
    return x, iteration_counter

minInterval = [-10, -10, -3]
maxInterval = [10, 10, 3]
eps = 1e-6

w_size = 0.2

funks = [f1, f2, f3]
roots = []
colors = ['r', 'b', 'g']
styles = ['ro' , 'bo', 'go']
#find all roots within the defined interval

for i in range(3):
    print i
    f = funks[i]
    minValue = minInterval[i]
    maxValue = maxInterval[i]
    root = []
    
    xx = np.linspace(minValue, maxValue, 100)
    plt.figure(i+1)
    titleName = 'function nbr ' + str(i+1)
    plt.title(titleName)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xx, f(xx), colors[i])
    plt.plot(xx, np.zeros(len(xx)), 'k')
    
    w_start = minValue
    w_end = w_start + w_size
    
    while w_end <= maxValue:
    
        x0 = 0.5*(w_start+w_end)
        x1 = w_start + 0.01     
    
        x, iteration_counter = secant(f, x0, x1, eps, w_start, w_end)
        if iteration_counter != -1:
            root.append(x)
            
        w_start = w_end
        w_end = w_start + w_size
    
    print 'function nbr ' + str(i+1) + ' has the roots ' + str(root)
    roots.append(root)
    style = colors[i] + 'o'
    for j in range(len(root)):
        # it refused plt.plot(root, f(root))
        plt.plot(root[j], f(float(root[j])),style)


 # printout when I ran it
#function nbr 1 has the roots [0.9577209358692776]
#function nbr 2 has the roots [] (so no roots)
#function nbr 3 has the roots [-1.1768884491713507]  
    
    
    
    
    
    
    
    
    
    
    
    
    
    