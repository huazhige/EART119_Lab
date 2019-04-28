# -*- coding: utf-8 -*-
"""
Brendan Chapman
EAR119
HW1
"""
#========================================================================================================================
" Question 1"
"Program computing the area of a rectangle"
#========================================================================================================================
'Variables'
C= 10
B= 5
'Computation'
Ar=(B*C)
print Ar
"Program computing the area of a triangle"
'Variables'
Hb=
B=
'Computation'
At=0.5*(Hb*B)
print At
#========================================================================================================================
" Question 2"
"Program computing area of an irregular polygon" 
#========================================================================================================================
'Variables'
x1=1
y1=1
x2=3
y2=1
x3=4
y3=2
x4=3.5
y4=5
x5=2
y5=4
'Computation' 
A= 0.5*(((x1*y2)+(x2*y3)+(x3*y4)+(x4*y5)+(x5*y1))-((y1*x2)+(y2*x3)+(y3*x4)+(y4*x5)+(y5*x1)))
print A
#========================================================================================================================
" Question 3"
"Program computing largest possible integer 'b' that matches the area of a circle 12.6mm in radius"
#========================================================================================================================
'Variables'
r=12.6
a=1.5
b=0
Ar=a*b  
Ac=(3.14*(r**2))
'Computation' 
print Ac
b= 498.5/1.5
print b
while Ac < Ar:
    b += 1
    print b

#========================================================================================================================
" Question 4"
"Program computing remaining 14C using radioactive decay equation "
#========================================================================================================================
'Part a' 
l= 5750
N0=0.0000
t=0
N=N0**(-t/l)
print N
'Part b'
from numpy import linspace 
from math import *
linspace(10000, 100000,10000)
t1=10000
t2=100000
t3=1000000
N10=(N0*e.real**-(t1/l))
print N10
N100=N0*e.real**-(t2/l)
print N100
N1000=N0*e.real**-(t3/l)
print N1000
'Part C'
N=N0*(e.real**(-(input/l)))
 







