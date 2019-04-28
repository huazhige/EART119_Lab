# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:23:48 2019

@author: bruno
"""
#import the math packet
import math

halfLife = 5730 #the half life

x = input("Enter a value for the half-life") #user input forthe half-life
y = input("Enter a value for the time") # User input for the time


def remAmount(No, time, halfLife):
    if(No == ""): #if an initial amount is not given then this task will be performed
        return  math.exp(-time/halfLife)
    else: # if an inital amount is given this task will be performed
        return No * math.exp(-time/halfLife)
           
print "The fractional amount remaining after 10,000 years is: %1.3f" % remAmount("", 10000 , halfLife)
print"The fractional amount remaining after 100,000 years is: %1.3f" % remAmount("", 100000 ,halfLife) 
print"The fractional amount remaining after 1,000,000 years is: %1.3f" % remAmount("", 1000000 ,halfLife) 

print "After entering %1.3f for the time and %1.3f for the half life, the fractional amount remaining is %1.3f" % (y,x,remAmount("", y, x))


