#!python3
t0= 2.5
c = 1.1 
A = 5
tstar = -10 
tend = 10
def Newton(F, dF,t, error, attempts):
    #cross-over when the difference btw. func. is zero
    i = 0
    while i < attempts:
        if abs(f(t)) < error:
            return t
        if g(t) == 0:
            print('Zero derivative. No solution found.')
            return None
        t = t - (c*(t - t0)**2 - A*t - t0)/(2*c*(t-t0)-A)
        i +=1
    return t
f = lambda t: c*(t - t0)**2 
g = lambda t: A*t + t0
F = lambda t: t - (c*(t - t0)**2 - A*t - t0)
dF = lambda t: 2*c*(t-t0)-A
error = 1e-6
attempts = 100
Newton(F, dF, 0, error, attempts)





