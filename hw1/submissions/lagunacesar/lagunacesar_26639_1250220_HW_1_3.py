# -*- coding: utf-8 -*-
'''
Cesar Laguna
Python 3.6
'''
import numpy as np
'''
# 3
Finding the minimum value of side b of a rectangle that will give us the 
the a number as close to but less than the area of the circle
'''
radius = 12.6
area_cir = np.pi*(radius**2)

a_rec = 1.5
b_rec = 0
while a_rec*b_rec < area_cir:    #will check and see if area of rec is smaller than area of circ
    b_rec = b_rec + 1   #if area of rec IS smaller then cir, then b gets +1 and this continues if area of 
                        #rec is smaller than area of cir until area of rec is larger than area of circ
b_rec = b_rec - 1   #need to subtract 1 because while loop gives a b vlaue that makes area of rec larger 
                    #than area of circ and we want slighly smaller than circle
print ('Laregst b value possible b=%.2f'%(b_rec))
