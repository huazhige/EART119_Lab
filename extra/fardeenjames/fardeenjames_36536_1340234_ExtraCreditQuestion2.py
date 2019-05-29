import numpy as np
import matplotlib.pyplot as plt


def fct_f(x):
    return np.sin(x)

xmin_f = 0
xmax_f = np.pi


def fct_g(x):
    return 2*x*(np.e)**x**2

xmin_g = 0
xmax_g = 1


x_values_f = np.linspace(xmin_f, xmax_f, 1000)
x_values_g = np.linspace(xmin_g, xmax_g, 1000)

y_values_f = fct_f(x_values_f)
y_values_g = fct_g(x_values_g)

delta_x_f = np.linspace((np.pi)/1000, (np.pi)/1000, 1000)
delta_x_g = np.linspace(0.001, 0.001, 1000)

f_Int = np.dot(delta_x_f, y_values_f)
g_Int = np.dot(delta_x_g, y_values_g)


print('Integral of f: ', f_Int)
print('Integral of g: ', g_Int)