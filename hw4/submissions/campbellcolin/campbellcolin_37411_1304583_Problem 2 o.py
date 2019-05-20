import numpy as np
import matplotlib.pyplot as plt

tmin, tmax = -10, 10
t0 = 2.5
c = 1.1
A = 5
tol = 1e-6
eps = 0.1
N = 100
sampsize = 1000
samp = np.linspace(tmin, tmax, sampsize)
sol = []
uni = []

def fct_f(t):
    return c * (t - t0)**2

def fct_g(t):
    return A * t + t0

def fct_diff(t):
    return fct_f(t) - fct_g(t)

def my_Secant(fct, x0, x1, tol = 1e-5, N = 20):
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        # numerical approx. of derivative
        dfdt = (fct(x1) - fct(x0))/(x1 - x0)
        # basically Newton
        x_next = x1 - fct(x1)/dfdt
        
        x0 = x1
        x1 = x_next
        
        i+= 1
    # check of solution converged
    if abs(fct(x1)) < tol:
        return x_next
    else: 
        return np.nan

def my_Newton(fct, df_dx, x0):
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 0
    while abs(fct(xn)) < eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan

for i in range(sampsize - 1):
    sol.append(round(my_Secant(fct_diff, samp[i], samp[i+1], tol, N), 3))
    if not(sol[i] in uni):
        uni.append(sol[i])

a_ft = fct_f(samp)
a_gt = fct_g(samp)
sel = abs(a_ft - a_gt) < eps

print('There are ' + str(len(uni)) + 'roots.')
print('They are (suing Secant Method): ')

for i in uni:
    print('t = ' + str(i) + ' with f(t) = ' + str(fct_f(i)) + ', g(t) = ' + str(fct_g(i)))

print('Crossover points using array method:')
print('Arrays of t, f(t), and g(t) values respectively', samp[sel], a_ft[sel], a_gt[sel])
print('The graph shows the difference function and two points for the calculated root using Newton Method')

plt.plot(samp, a_ft - a_gt, 'go', ms = 2)
plt.plot(uni[0], fct_f(uni[0]), 'ko')
plt.plot(samp[sel][0], a_ft[sel][0] - a_gt[sel][0], 'ro')
plt.savefig('graphrootcomparison.png')
plt.show()
















