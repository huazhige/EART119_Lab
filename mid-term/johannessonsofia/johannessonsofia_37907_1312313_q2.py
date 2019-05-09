# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#functions
def Newton(f, dfdx, x, eps, xmin, xmax):
    f_value = f(x)
    iteration_counter = 0
    inInterval = True
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value)/dfdx(x)
        except ZeroDivisionError:
            print "Error! - derivative zero for x = ", x
#            sys.exit(1) # Abort with error
        if x < xmin or x>xmax:
                inInterval = False
                
        f_value = f(x)
        iteration_counter += 1
        
    # Here, either a solution is found, or too many iterations
    if abs(f_value) > eps or inInterval==False:
        iteration_counter = -1
    return x, iteration_counter


#variables
    
def f1(x):
    return x**5+(2./5.)*x**2-2

def df1dx(x):
    return 5*x**4+(4./5.)*x

def f2(x):
    return np.exp(-0.1*x)+x

def df2dx(x):
    return (-0.1)*np.exp(-0.1*x)+1

def f3(x):
    return 10*np.sin(0.25*x)+0.1*(x+12)
    
def df3dx(x):
    return (10./4.)*np.cos(0.25*x)+0.1

funks = [f1, f2, f3]
ders = [df1dx, df2dx, df3dx]
eps = 1e-6
roots = []
colors = ['r', 'b', 'g']
styles = ['ro' , 'bo', 'go']
filenames = ['q2a', 'q2b', 'q2c']
#find all roots within the defined interval

for i in range(3):
    print i
    f = funks[i]
    dfdx = ders[i]
    minValue = -10
    maxValue = 10
    root = []
    
    xx = np.linspace(minValue, maxValue, 100)
    im = plt.figure(i+1)
    titleName = 'function nbr ' + str(i+1)
    plt.title(titleName)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(xx, f(xx), colors[i])
    plt.plot(xx, np.zeros(len(xx)), 'k')
    filename = filenames[i]
    
    
    w_start = minValue
    w_end = w_start + 0.2
    
    while w_end <= maxValue:
    
        x0 = 0.5*(w_start+w_end)    
    
        x, iteration_counter = Newton(f, dfdx,x0,eps, w_start, w_end)
        if iteration_counter != -1:
            root.append(x)
            
        w_start = w_end
        w_end = w_start + 0.2
    
    print 'function nbr ' + str(i+1) + ' has the roots ' + str(root)
    roots.append(root)
    style = colors[i] + 'o'
    for j in range(len(root)):
        # it refused plt.plot(root, f(root))
        plt.plot(root[j], f(float(root[j])),style)
        plt.text(root[j], f(3), 'root: ' + str(root[j]))
    im.savefig(filename)









