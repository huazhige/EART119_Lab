# imports
import numpy as np
import matplotlib.pyplot as plt

# parameters
the_range = np.linspace(-10, 10, 1000)

# functions
def func_1(x):
    return x**5+(2/5)*x**2-2

def func_2(x):
    return np.exp(-(x/10))+x

def func_3(x):
    return 10*np.sin(x/4)+0.1*(x+12)

def my_Secant(func, x0, x1, N):
    return #???


# plotting
plt.figure(1)
plt.axes()
plt.grid()
plt.plot(func_1(the_range))
plt.plot(func_2(the_range))
plt.plot(func_3(the_range))
plt.savefig('Question2_fig.png')
plt.show()