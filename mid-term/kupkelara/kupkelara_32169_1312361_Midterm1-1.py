#!/usr/bin/env python
# coding: utf-8

# In[55]:


#!python3

import numpy as np
import matplotlib.pyplot as plt


#functions
f1 = lambda x: x**5 + 2/5*x**2 - 2
x1_min = -10
x1_max = 10
f2 = lambda x: np.exp(-x/10) + x
x2_min = -10
x2_max = 10
f3 = lambda x: 10*np.sin(x/4) + 0.1*(x+12)
x3_min = -10
x3_max = 10

#manual variables
error = 1e-4
N = 100

#Find the roots
def secant(f, xmin, xmax, error):
    f0 = f(xmin)
    f1 = f(xmax)
    x0 = xmin
    x1 = xmax
    i = 0
    while abs(f1) > error and i < 100:
        if x1 - x0 == 0:
            print ('Error: x1 -x0 = 0')
            return None
        denominator = (f1 - f0)/(x1 - x0)
        if denominator == 0:
            print('Error: Denominator = 0)')
            return None
        if denominator == (f1 - f0)/(x1 - x0):
            x = x1 - f1/denominator
        x0 = x1
        x1 = x
        f0 = f1
        f1 = f(x1)
        i += 1
    return x

Eq1_root = secant(f1, x1_min, x1_max, error)
Eq2_root = secant(f2, x2_min, x2_max, error)
Eq3_root = secant(f3, x3_min, x3_max, error)



#pthe function arrays

xvec = np.linspace(-10,10,N)
f1vec = f1(xvec)
f2vec = f2(xvec)
f3vec = f3(xvec)

plt.figure(2)
ax2 = plt.subplot( 111)
plt.plot(xvec,f1vec)
plt.xlim(-10, 10)
plt.plot(Eq1_root,f1(Eq1_root),'ro', label=Eq1_root)
plt.legend(loc='upper left')
plt.show()

print('Equation 1:', Eq1_root)


plt.figure(3)
ax2 = plt.subplot( 111)
plt.plot(xvec, f2vec)
plt.xlim(-10, 10)
plt.plot(Eq2_root,f2(Eq2_root),'ro',label=Eq2_root)
plt.legend(loc='upper left')
plt.show()

print('Equation 2:', Eq2_root)

plt.figure(4)
ax2 = plt.subplot( 111)
plt.plot(xvec, f3vec)
plt.xlim(-10, 10)
plt.plot(Eq3_root,f3(Eq3_root),'ro',label=Eq3_root)
plt.legend(loc='upper left')
plt.show()

print('Equation 3:', Eq3_root)


# In[ ]:




