#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:02:30 2019

@author: jtbabbe

Write radioactive decay eqn.
"""

import math
#================================
# Define Variables
#================================

# Vars. for parts a and b
N = 1  # quantity
tao = 5730     
t1 = 10000    # years
t2 = 100000   # years
t3 = 1000000  # years

# Vars. for part c
taoUser = raw_input('What is your desired half-life? ')
tUser = raw_input('What is your desired decay time? ')



#=================================
# Define Functions
#=================================

def  f_radDecay ( N, tao, t):
    amount1 = N * math.exp(-(float(t)/float(tao)))
    print amount1, 'left'
  
    
def f_radDecay_user ( N, taoUser, tUser):
    amount2 = N * math.exp(-(float(tUser)/float(taoUser)))
    print "%.5f" %amount2, 'left'
     
#=================================
# Run functions
#================================
    
f_radDecay( N, tao, t1)
f_radDecay( N, tao, t2)
f_radDecay( N, tao, t3)

f_radDecay_user( N, taoUser, tUser)

