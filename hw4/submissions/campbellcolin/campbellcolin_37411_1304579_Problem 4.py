import numpy as np

def f1(x):
    return -(x**5)+(1/3)*x**2+(0.5)

def f2(x):
    return (np.cos(x))**2+0.1

def f3(x):
    return np.sin(x/3) + 0.1*(x+5)

def my_Secant(fct, x0, x1, tol = 1e-5, N = 20):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        # numerical approx. of derivative
        dfdt = (fct(x1) - fct(x0))/(x1 - x0)
        
        # basically Newton's method
        x_next = x1 - fct(x1)/dfdt
        
        x0 = x1
        x1 = x_next
        
        i+= 1
    # check of solution converged
    if abs(fct(x1)) < tol:
        return x_next
    else: 
        return np.nan

x1 = my_Secant(f1, 1, 10)
x2 = my_Secant(f2, -10, 10)
x3 = my_Secant(f3, -3, 3)

print(x1)
print(x2)
print(x3)