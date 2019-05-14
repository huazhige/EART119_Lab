# -*- coding: utf-8 -*-
'''
Cesar Laguna
Python 3.6
'''
import math as m
'''
# 4

'''
def remaining(time, half_life, initial = 1):  #creates a funtion that will provide the 
                                              #reaming amount
    N = initial*m.exp((-time)/half_life)
    return (N)

#part b
print (remaining(10000, 5730))
print (remaining(100000, 5730))
print (remaining(1000000, 5730))

#part c
def remaining_own_input():
    time = int(input('Enter time elapsed   :'))
    half_life = int(input('Enter half life  :'))
    initial = (input('Enter initial amount  :'))
    if initial == '':  #if no value id inputted then innital will be set to 1
        initial = 1
    N = initial*m.exp((-time)/half_life)
    return (N)
print(remaining_own_input())