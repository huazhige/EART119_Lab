# -*- coding: utf-8 -*-


#=====================================
# import
#=====================================

import numpy as np
import matplotlib.pyplot as plt

#=====================================
# definitions
#=====================================

file_in = 'midterm_dydx.txt'

mData = np.loadtxt(file_in).T

t = mData[0]
zt = mData[1]

delta = 1

def derivative ( t,  zt, delta):
    dzdt_CD = np.array([])
    dzdt_CD = np.append(dzdt_CD,0)
    for i in range (0, len(zt)-2):
        if (i == 0):
            #compute forward der
            dzdt_FD = (zt[(i+delta)] - zt[(i)])/(t[i+1]-t[i])
            dzdt_CD = np.append(dzdt_CD,[dzdt_FD])
        elif (i>=len(zt)-1):
            #compute backward der
            dzdt_BD = (zt[(i)] - zt[(i-delta)])/(t[i]-t[i-1])
            dzdt_CD = np.append(dzdt_CD,[dzdt_BD])
        else:        
           dzdt_CD = np.append(dzdt_CD, [(zt[(i + delta)] - zt[(i-delta)])/(2*(t[i+1]-t[i]))])
    return np.append(dzdt_CD,0)

der1 = derivative( t, zt, delta)
der2 = derivative( t, der1, delta)

#=====================================
# plot
#=====================================
    
plt.figure(1)
plt.plot( t, zt, 'k-')
plt.grid(True)
plt.xlabel( 't')
plt.ylabel( 'Fct Values z(t)')
plt.show()


plt.figure(2)
plt.plot( t, der1, 'r-')
plt.grid(True)
plt.xlabel( 't')
plt.ylabel( "Fct Values z'(t)")
plt.show()

plt.figure(3)
plt.plot( t, der2, 'g-')
plt.grid(True)
plt.xlabel( 't')
plt.ylabel( "Fct values z''(t)")


