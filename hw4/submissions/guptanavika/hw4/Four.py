def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x_next
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        print i, abs( fct( x1)), x_next
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)



import math
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 1000)

t=np.linspace(-10, 10, 1000)


def f1(x):
    return -(x**5)+(1/3)*(x**2)+1/2


def f2(x):
    return ((np.cos(x)**2) + 0.1)

#y=f2(math.pi)

#print y
def f3(x):
    return np.sin(0.3333*x)+0.1*(x+5)



plt.subplot(211)
plt.plot( x, f1(x), 'r-')

plt.subplot(212)
plt.plot(x, f2(x), 'g-')

#plt.subplot(213)

plt.plot(t, f3(t), 'b-')

plt.show()


print "roots for eq1:"
root=my_Secant( f1, -10, 10, tol = 1e-4, N = 20)
print root
print "roots for eq2:"
root1=my_Secant( f2, -2, 1, tol = 1e-4, N = 20)
print root1
print "roots for eq3:"
root2=my_Secant( f3, -3, 3, tol = 1e-4, N = 20)
print root2
