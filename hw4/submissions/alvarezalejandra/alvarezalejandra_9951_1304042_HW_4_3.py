import numpy as np

def dh(h, t):
    return abs(0 - h(t))


roots = []
def newton_method(h, dh, x0, tol):
    delta = dh(h , x0)
    while ( x0 - delta) < tol: #tol (tolerance) is the same as epsilon this time < tol
        #print("Going")
        x0 = x0 - h(x0)/dhdt(x0)
        delta = dh(h , x0)
        #print(delta)
    #print ('Root is at: ', x0)
    #print ('f(x) at root is: ', f(x0))
    if round(x0, 3) not in roots: #rounding numbers to make it easier to work with
        roots.append(round(x0, 3))

    
x0s = np.linspace(-10, 10, 20)  #calling function
for x0 in x0s:
    newton_method(h, dh, x0, 1e-5)

roots = np.asarray(roots)
froots = f(roots)

print(roots)
print(froots)

