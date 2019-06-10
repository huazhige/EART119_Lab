#! python3
"""Hw 5 Problem 2
Part 1 is copy pasted with variables changed and some removals.
y''+w0**2*y = Fcos(wt)
"""
import numpy as np
import matplotlib.pyplot as plt

####Part 1####

F = 0.5
w =1
w0 = .999
h= 0.1

# part b:
#solve for c1 and c2

#y = c1*cos(w0*t) + c2*sin(w0*t) + [F/(w0**2-w**2)]cos(w*t)

y = lambda t: c1*np.cos(w0*t) + c2*np.sin(w0*t) + [F/(w0**2-w**2)]*np.cos(w*t)
dy = lambda t: -c1*w0*np.sin(w0*t)+c2*w0*np.cos(w0*t)-(f*w*np.sin(w*t))/(w0**2-w**2)

c1 = -F/(w0**2-w**2)
c2 = 0

#part c:
#write the general solution as a product of sins
# -c1 = [F/(w0**2-w**2)]
# c1*cos(w0*t) - c1*cos(w*t)
y = lambda t: c1*(-2*np.sin((w*t+w0*t)/2)*np.sin((w0*t-w*t)/2)) #composite function

y1 = lambda t:c1*(-2*np.sin((w*t+w0*t)/2)) #forcing function 1
y2 = lambda t: c1*np.sin((w0*t-w*t)/2) #forcing function 2

#part e: numerical solutions (part d is afterwards for organizational reasons)

#def function
def function(t,y, F = 0.5, w = 1, w0 = 0.8):
    return F*np.cos(w*t)-(w0**2)*y

#def euler_forward(funct, t, h):
def euler_forward(funct, y_initial, t_range, h):
    """ 
    input:
        funct: ODE 
        y_initial: conditions at t_range[0], type = array
        t_range: first and last t value
        h: step size
    output:
        t_sol: time in steps of h
        y_sol: computed y value at each t point
    """
    degree = len(y_initial)
    N = int((t_range[-1]-t_range[0])/h) #interval size
    t = t_range[0]
    y0 = y_initial[0]
    y1 = y_initial[1]
#    y = y_initial
    
    #array to contain solutions
    t_sol = np.zeros(N)
    t_sol[0] = t

    y_sol = np.zeros(N)
    y_sol[0] = y0
    t+=h
    
    for i in range(1,N):
        y1 += h*funct(t, y0)
        y0 += h * y1
        t += h
#        print(y0)
        y_sol[i] = y0
#        print(y_sol)
        t_sol[i] = t

    return t_sol, y_sol


#Part d: plotting

vec_t = np.arange(0, 5000*np.pi, h)
vec_y = y(vec_t)
vec_y1 = y1(vec_t)
vec_y2 = y2(vec_t)
te, ye = euler_forward(function, [0,0], vec_t, h)

#plot analytical solution
fig,ax=plt.subplots(2)

ax[0].set_title('Problem 2')
ax[0].plot (vec_t, vec_y, color = 'blue', label = 'Composite analytical solution')

#plot forcing funciton
ax[0].plot (vec_t, vec_y1, color = 'grey', alpha =0.5, label = 'Forcing function 1')
ax[0].plot (vec_t, vec_y2, color = 'green', alpha = 0.5, label = 'Forcing function2')

#plot numerical solution
ax[0].plot(te,ye, color = 'pink', alpha = 0.8, label = 'Numerical Solution by Euler Forward')

#plot differences (Part f)
vec_diffe = abs(vec_y[2:] - ye[1:])
ax[1].plot(vec_t[2:], vec_diffe, label = 'Difference between analytical and euler')
ax[1].legend(loc = 'best')

#exact solution for w = w0 part h
e = lambda t: c1*np.cos(w0*t)+c2*np.sin(w0*t)+F/(2*w0)*t*np.sin(w0*t)
vec_e = e(vec_t)
ax[0].plot(vec_t, vec_e, color = 'orange', alpha = 0.5, label = 'Exact solution when w0~w') #the exact solution
dif_vec = abs(vec_e[1:] - ye)
ax[1].plot(vec_t[1:], dif_vec, color = 'blue', alpha = 0.5, label = 'The difference btw exact and euler') #the difference

#legend
ax[0].legend(loc='best')

ax[1].legend(loc = 'best')
plt.show()

"""
Part g
As w0~w, forcing funciton 1 drastically increases in amplitude.
Forcing funciton 2, seems to become negatively linear. In actuality it has become even
slower. Euler's method becomes useless.

Part h
The exact solution starts out larger but starts its growth slower.
Part J:
w~w0 does not seem to work with the Hook's law derivation. The natural osccillations cause issues.
Hooke's law holds for most springs as long as the displacement is within proportionality.
When the resonant frequency is achieved the spring will oscillate at a large amplitude. As time goes on the 
amplitude steadily increases, until the spring breaks. The aproximation slows down eventually.
"""

"""Quick summary:
There are three images for this part. They show that the exact solution seems to drive endlessly, while 
the aproximation still is shaped by the driving funcitons.
"""
