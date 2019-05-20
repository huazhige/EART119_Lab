# -*- coding: utf-8 -*-
"""
HW 4 problem 5
Benjamin Zhu 1696575
Pf. Tomas Goebel 
Astro/Earth 119

Finding velocity and accleration at everypoint using 
data of position and time
Plot all three on the same graph
"""

#=======================================================
#           imports and files
#=======================================================

import numpy as np
import matplotlib.pyplot as plt
import os

s_t     = np.loadtxt('HW4_vertTraj.txt').T

#=======================================================
#           variables
#=======================================================

t       = s_t[0]
s       = s_t[1]

#=======================================================
#           velocity 
#=======================================================

N   = len(t)
i   = 0
v   = []

while i <= N:
    if i == 0:
        vt = (s[i+1]-s[i]) / (t[i+1]-t[i]) #the first element has nothing
        v.append(vt)                        #beofre it, so I used F. difference
    elif N-1 > i > 0:
        vt = (s[i+1]-s[i-1]) / (t[i+1]-t[i-1])
        v.append(vt)
    elif N-1 == i:
        vt = (s[i]-s[i-1]) / (t[i]-t[i-1]) #the last element is cut off
        v.append(vt)                        # so I'm using B. differnece
    i += 1

#=======================================================
#           acceleration
#=======================================================
    
i   = 0
a   = []

while i <= N:
    if i == 0:
        at = None   #I really don't know how to get this...
        a.append(at)
    elif N-1 > i > 0:
        at = (s[i+1]-2*s[i]+s[i-1]) / (t[i+1]-t[i])**2
        a.append(at)
    elif N-1 == i:
        at = None   #No idea on the end either.... 
        a.append(at)
    i += 1

    
"""
So appearanly I could just do exactly what I did on the first part
to find velocity against time.I attached it below. I didn't use it because it 
gave me a result that is very off from the rest at t = 0 and t = 1, making the
graph ugly.

while i <= N:
    if i == 0:
        at = (v[i+1]-v[i]) / (t[i+1]-t[i]) #the first element has nothing
        a.append(at)                        #beofre it, so I used F. difference
    elif N-1 > i > 0:
        at = (v[i+1]-v[i-1]) / (t[i+1]-t[i-1])
        a.append(at)
    elif N-1 == i:
        at = (v[i]-v[i-1]) / (t[i]-t[i-1]) #the last element is cut off
        a.append(at)                        # so I'm using B. differnece
    i += 1
"""
    
 
#=======================================================
#           plotting
#=======================================================       
ax = plt.subplot()
ax.plot( t, s, label='position')
ax.plot( t, v, 'b', label='velocity')
ax.plot( t, a, 'r', label='acceleration')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.xlabel('t')
os.chdir('prob5_figure')
plt.savefig('prob5')





































