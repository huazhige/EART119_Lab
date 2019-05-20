# -*- coding: utf-8 -*-
"""
HW4 Problem 2: 
  Find the intersection (cross-over point)between the following two functions using 
  Newton’s or the Secant method (Hint: solve for f(t)−g(t)=0)! 
  •f(t)=c(t−t0)^2, with t0= 2.5, c = 1.1, and −10≤t≤10
  •g(t)=At+t0, with A= 5, and −10≤t≤10
    a)How many cross-over points are there for −10≤t≤10? 
    b)What are the values
    of t, f(t)and g(t)?
    c)Compare your solutions with the solutionfrom week 2 
    (in class assignment inC_2_1_vec_matrix.pdf, functions and vectors). 
    For the comparison: plot f(t)−g(t) and one of the cross-over points detected with both methods. 
    You may have to zoom a bit to see the difference. Save the plot as .png
    and submit to canvas.   
"""
import numpy as np  
import matplotlib.pyplot as plt   
import os
import opt_utils

#==============================================
        #Variables, functions
#==============================================                
dir_out_newt = 'C:\Users\Connor\OneDrive\ASTR 119\Homework\HW4'
N     = 20
t0    = 2.5
c     = 1.1
tmin  = -10
tmax  = 10
a_t   = np.linspace(tmin, tmax, N)
A     = 5

def f( t, c, t0):    
    return c*(t - t0)**2
def g( t, A):
    return A*t + t0

def fct(t):
    return c*(t - t0)**2 - (A*t + t0)    

def df_dt( t):
    return 2*c*(t - t0) - A





#==============================================
        #Solving for crossover points
#==============================================
for t in range( -10, 10):
    opt_utils.my_Newton( fct, df_dt, t, tol = 1e-5, N = 20)
    t += 1
t_1, t_2 = 0.4366, 9.1088 
print "Crossover Points at t=", t_1, ',', t_2 
     
  
#==============================================
        #Plotting
#==============================================   
plt.plot( a_t, f( a_t, c, t0), 'o-', mec = 'r', ms = 2, mfc = 'none', label = 'f(t)')
plt.plot( a_t, g( a_t, A), 'o-',     mec = 'b', ms = 2, mfc = 'none',  label = 'g(t)')
#plt.plot( a_t, g2_t( a_t, A, t0), 'o', mec = 'g', ms = 2, mfc = 'none',  label = 'g2(t)')
plt.xlabel( 't [units]')
plt.ylabel( 'Position [units]')
plt.legend()
os.chdir( dir_out_newt)   
plt.savefig( 'dir_out_newt')
plt.show()



"""
plt.plot( fct(t), t, 'r-')
plt.xlabel( 'f(t)')
plt.ylabel('g(t)')
plt.show()
"""