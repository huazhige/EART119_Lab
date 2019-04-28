#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing math
import math

# Part (a)
# Function for the remaining amount
# The arguments include the time elapsed, half-life, and optionally the initial amount
def remained(time, half_life, initial = 1):
    # Formula for the remaining amount
    N = initial*math.exp((-time)/half_life)
    
    # Returns the remaining amount
    return N

# Part (b)
# Prints the remaining amount for several cases
print(remained(10000, 5730))
print(remained(100000, 5730))
print(remained(1000000, 5730))

# Part (c)
# Function for the remaining amount with user input
# No arguments included since the user is inputting them
def input_remained():
    # User inputs for time and half-life
    time = float(input("Please enter the time elapsed: "))
    half_life = float(input("Please enter the half-life: "))
    
    # User input for the initial amount, which can be skipped by pressing enter
    initial = input("Please enter the initial amount (skip for fractional amount remaining): ")
    
    # If skipped, the initial amount becomes the exponent alone
    # Otherwise, the inputted initial amount is converted to a float
    if initial == "":
        initial = 1
    else:
        initial = float(initial)
        
    # Formula for the remaining amount
    N = initial*math.exp((-time)/half_life)
    
    # Returns the remaining amount
    return N

