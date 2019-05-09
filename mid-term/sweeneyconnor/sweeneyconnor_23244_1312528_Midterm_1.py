# -*- coding: utf-8 -*-
"""
Midterm #1

Star Luminosity
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as ou
#===================================
#         Load Data  
#===================================
data_dir = 'C:\Users\conma\OneDrive\ASTR 119\My programs\Midterm'
file_in  = 'star_luminos.txt'
m_Data   = np.genfromtxt( file_in, usecols = (0,1), skip_header = 1 ).T  #Load data file 



#===================================
#         Variables  
#===================================
Temp       = m_Data[0] 
Lumin      = m_Data[1]
Tmin, Tmax = 0, 1000

least_sqr = ou.lin_LS( Temp, Lumin)
#pl_fit     = 


plt.plot( Temp, Lumin, 'ko', label = 'Raw Data')    
plt.plot( Temp, least_sqr(4), 'r-', label = 'Best Fit')    
plt.legend()
plt.show()
print least_sqr


