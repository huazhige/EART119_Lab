# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:15:34 2019

@author: Hobo
"""
#========================================================================================================================
" Question 4"
""" Find the roots of four functions"""
#========================================================================================================================


'Variables'
# Program to find root of
# equations using secant method

import numpy as np
import matplotlib.pyplot as plt

# function takes value of x
# and returns f(x)
"a" 
def f(x):((-x**5)+((1/3)*((x**2))+(1/2))
    


#return f;

#def secant(x1, x2, E):
  #n = 0; xm = 0; x0 = 0; c = 0;
   
if (f(x1) * f(x2) < 0): 
    while True: 
        # calculate the intermediate value x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)));
        x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
        # check if x0 is root of # equation or not c = f(x1) * f(x0);
        c = f(x1) * f(x0)
        # update the value of interval x1 = x2; x2 = x0; 
        x1 = x2; x2 = x0; 
        # update number of iteration n += 1;
        n += 1
        # if x0 is the root of equation 
        # then break the loop if (c == 0):
        break; xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); 
        if(abs(xm - x0) < E): break; 
        print("Root of the given equation =", round(x0, 6)); print("No. of iterations = ", n);
        #else print("Can not find a root in ", "the given inteval");
"b"
def f(x):((cos**2(x))+ 0.1
     
    


#return f;

#def secant(x1, x2, E):
  #n = 0; xm = 0; x0 = 0; c = 0;
   
if (f(x1) * f(x2) < 0): 
    while True: 
        # calculate the intermediate value x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)));
        x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
        # check if x0 is root of # equation or not c = f(x1) * f(x0);
        c = f(x1) * f(x0)
        # update the value of interval x1 = x2; x2 = x0; 
        x1 = x2; x2 = x0; 
        # update number of iteration n += 1;
        n += 1
        # if x0 is the root of equation 
        # then break the loop if (c == 0):
        break; xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); 
        if(abs(xm - x0) < E): break; 
        print("Root of the given equation =", round(x0, 6)); print("No. of iterations = ", n);
        #else print("Can not find a root in ", "the given inteval");

"c"
def f(x):((sin(x/3))+(0.1((x+5))))
    


#return f;

#def secant(x1, x2, E):
  #n = 0; xm = 0; x0 = 0; c = 0;
   
if (f(x1) * f(x2) < 0): 
    while True: 
        # calculate the intermediate value x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)));
        x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
        # check if x0 is root of # equation or not c = f(x1) * f(x0);
        c = f(x1) * f(x0)
        # update the value of interval x1 = x2; x2 = x0; 
        x1 = x2; x2 = x0; 
        # update number of iteration n += 1;
        n += 1
        # if x0 is the root of equation 
        # then break the loop if (c == 0):
        break; xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); 
        if(abs(xm - x0) < E): break; 
        print("Root of the given equation =", round(x0, 6)); print("No. of iterations = ", n);
        #else print("Can not find a root in ", "the given inteval");
