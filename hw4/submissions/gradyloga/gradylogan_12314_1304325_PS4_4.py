# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils


x  = np.linspace(-10, 10, 1000)
x1 = np.linspace(-3, 3, 1000)



def f1(x):
    return -x**5+(x**2)/3+.5
#with -10 to 10


def f2(x):
    return (np.cos(x)**2)+.1
#with -10 to 10


def f3(x1):
    return (np.sin(x1/3))+(.1*(x1+5))
# with -3 to 3



root1 = opt_utils.my_Secant( f1, -1, 1, tol = 1e-7, N = 100)
root2 = opt_utils.my_Secant( f2, -10, 10, tol = 1e-4, N = 20)
root3 = opt_utils.my_Secant( f3, -3, 3, tol = 1e-4, N = 20)


plt.figure()
p1 = plt.subplot(311)
p1.plot(x, f1(x), 'r-')
p1.plot([root1], [f1(root1)], 'r*', ms = 15)

p2 = plt.subplot(312)
p2.plot(x, f2(x), 'b-')
p2.plot([root2], [f2(root2)], 'b*', ms = 15)

p3 = plt.subplot(313)
p3.plot(x1, f3(x1), 'k-')
p3.plot([root3], [f3(root3)], 'k*', ms = 15)

print root1
print root2
print root3


