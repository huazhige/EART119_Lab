#! python3
"""Hw 5 Problem 1
y''+w0**2*y = Fcos(wt)
"""
import numpy as np
import matplotlib.pyplot as plt

####Part 1####

F = 0.5
w =1
w0 = 0.8
h= 0.4

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

vec_t = np.arange(0, 55*np.pi, h)
vec_y = y(vec_t)
vec_y1 = y1(vec_t)
vec_y2 = y2(vec_t)
te, ye = euler_forward(function, [0,0], vec_t, h)

#plot analytical solution
fig,ax=plt.subplots(2)

ax[0].set_title('Problem 1')
ax[0].plot (vec_t, vec_y, color = 'blue', label = 'Composite analytical solution')

#plot forcing funciton
ax[0].plot (vec_t, vec_y1, color = 'grey', alpha =0.5, label = 'Forcing function 1')
ax[0].plot (vec_t, vec_y2, color = 'green', alpha = 0.5, label = 'Forcing function2')

#plot numerical solution
ax[0].plot(te,ye, color = 'pink', alpha = 0.8, label = 'Numerical Solution by Euler Forward')
#legend
ax[0].legend(loc='best')

#plot differences (Part f)
vec_diffe = abs(vec_y[2:] - ye[1:])
ax[1].plot(vec_t[2:], vec_diffe, label = 'Difference between analytical and euler')
ax[1].axhline(y =1,color = 'green', label = 'Reference for one unit difference')
ax[1].legend(loc = 'best')
plt.show()


"""
Part f
For the given time frame, h at = 0.4 provides a difference less than 1 unit using the euler method. It seems 
accurate enough for three periods at least.
The further one goes from zero the greater the error becomes.
"""

"""Quick summary:
F affects the amplitude.
Higher w causes higher frequency.
w0 also affects the amplitude and general shape
"""
