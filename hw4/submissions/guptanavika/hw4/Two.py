import numpy as np
import matplotlib.pyplot as plt


def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)






#y=c*(t-tNot)**2
tNot=2.5
c=1.1

A=5

N=1000
t = np.linspace(-10, 10, 1000)

def f(t):	
	return (1.1)*(t - (2.5))**2

def g(t):
	return (5)*t+(2.5)


 
def minus(t):
	return ((1.1)*(t - (2.5))**2)-((5)*t+(2.5))

def dMinus(t):
	#return ((-2)*(c)*(t - (tNot)))-(A)
	return 2.2*t-10.5

plt.figure()
plt.plot( t, f(t), 'r-')
plt.plot(t, g(t), 'g-')

plt.show()

# As the graph shows there are two cross over points

root1=my_Newton(minus, dMinus, 10,tol = 1e-4, N = 20)
root2=my_Newton(minus, dMinus, -10,tol = 1e-4, N = 20)

print "Points:"

print root1
print root2


plt.figure(2)
plt.plot(t, minus(t), 'b-')
#plt.plot(root1, g(root1), 'r.')
plt.plot(root2, f(root2), 'r.')
plt.show()

# for t in range(-10,10):

	
# 	if(x==y):
# 		count=count+1
	


# print count