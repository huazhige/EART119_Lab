# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:41:09 2019
Earth 119 HW1 Problem #4
@author: Benny Quiroz
"""


import numpy 
#Part A
def rdecay(t, halflife, i_amount = 1):
    #i_amount is keyworded to one so that if no amount is given,
    #the fractional amount is still returned
    #Computes the amount remaining step by step using a variable ans
    ans = float(-1*t)
    ans = ans/float(halflife)
    ans = numpy.e**(ans)
    ans = i_amount*ans
    return ans

#Part B 
    #If  I understand the question, this is just test code for the above function.

print rdecay(10000, 5370)
print rdecay(100000, 5370)
print rdecay(1000000, 5370)

#Part C
#Just gives simple prompts in console and calls the function with the answer values.
inptime = input("How long has it been? ")
inphlife = input("What is the halflife of the sample? ")
print rdecay(inptime, inphlife)