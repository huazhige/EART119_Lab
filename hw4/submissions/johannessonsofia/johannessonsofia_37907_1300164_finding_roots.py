# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#===============================================
#               functions
#===============================================
c = 1.1
t_0 = 2.5
A = float(5)

def f(t):
    f = c*(t-t_0)**2
    return f

def g(t):
    g = A*t+t_0
    return g

def diff_fg(t):
    fvalue = f(t)
    gvalue = g(t)
    return fvalue-gvalue

def dfuncdx(t):
    dfdx = 2*c*t - 2*c*t_0
    dgdx = A
    return dfdx-dgdx

#from book
def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value)/dfdx(x)
        except ZeroDivisionError:
            print "Error! - derivative zero for x = ", x
#            sys.exit(1) # Abort with error
                
        f_value = f(x)
        iteration_counter += 1
        
    # Here, either a solution is found, or too many iterations
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

#from book
def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    x0 = float(x0)
    x1 = float(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = float(f_x1 - f_x0)/(x1 - x0)
            x = x1 - float(f_x1)/denominator
        except ZeroDivisionError:
            print "Error! - denominator zero for x = ", x
#            sys.exit(1) # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps:
        iteration_counter = -1
    return x, iteration_counter

#===============================================
#                   parameters
#==============================================
c = 1.1
t_0 = 2.5
A = 5
t = np.linspace(-10,10,700)
eps = 0.0001
tmin = -10
tmax = 10


#================================================
#                   computations
#================================================

#first root, maybe do a while loop instead
x0 = t[len(t)/2] #initial guess in the middle of the interval
x1 = t[len(t)/2 +1]
xNewton1, counts = Newton(diff_fg, dfuncdx, x0, eps)
xSecant1, counts = secant(diff_fg, x0, x1, eps)
ans = ('Newtons method, root ' + str(xNewton1) + ' in ' +str(counts) +' iterations')
print ans

print ('Secants method, root ' + str(xSecant1) + ' in ' +str(counts) +' iterations')
print ('f(t)=' + str(c*(xSecant1-t_0)**2) + ' and g(t) = ' + str(A*xSecant1+t_0))


#second root
x0 = t[-2]
x1 = t[-1]
xNewton2, counts = Newton(diff_fg, dfuncdx, x0, eps)
xSecant2, counts = secant(diff_fg, x0, x1, eps)
print ('Newtons method, root ' + str(xNewton2) + ' in ' +str(counts)+ ' iterations')
print ('Secants method, root ' + str(xSecant2) + ' in ' +str(counts) +' iterations')
print ('f(t)=' + str(c*(xSecant2-t_0)**2) + ' and g(t) = ' + str(A*xSecant2+t_0))

#compare w method from in class example, using vector method
f_vec = f(t)
g_vec = g(t)
diff_vec = f_vec-g_vec

sel =abs(diff_vec)<0.1
#print diff_vec

print ('vector method ' + str(t[sel]) )
roots = t[sel]

im = plt.figure(1)
plt.plot(t, diff_fg(t), 'r-')
plt.plot(t, np.zeros(len(t)), 'b-')

im2 = plt.figure(2)
#find index of my root so I can make a new window more zoomed in
idx = np.where(t>=xSecant1)
idxValue = idx[0][0]

window = 5
tnew =np.linspace(t[idxValue-window], t[idxValue+window], 2*window+1)


plt.plot(tnew, f(tnew), 'b')
plt.plot(tnew,g(tnew),'r')

plt.plot(xSecant1, f(xSecant1), 'k o')

plt.plot(roots[0], f(roots[0]), 'g o')
plt.xlabel('t')
plt.ylabel('function value')
plt.title('First intersection point')
t = plt.text(0.37, 5.39, 'Secants method', horizontalalignment='left', size='large', color='black')
t = plt.text(0.37, 5.2, 'Vector method', horizontalalignment='left', size='large', color='green')
im2.savefig('HW4_q2.png')

