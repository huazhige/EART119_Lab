# -*- coding: utf-8 -*-
"""

Code by Jason Minera
using python 2.7
due 4/14/19

Question:
Write a program that computes the area of a rectangle (A=bc) and the area of a
triangle (A = 0.5*hbb). The input of your function will be b and c for the 
rectangle and hb and b for the triangle

"""
'''
using python 2.7 with spyder

I want to ask the user the lengths of the rectangle and triangle and make the code find the area of said lengths.
'''
print('----------------------------------------------------------\n Hello we will be calculating the the area of a rectangle.\n---------------------------------------------------------- ' )

b = input('\n How long is the length of your rectangle in cm?  ' )  #this is asking the user for an input of the length of the rectangle.

c = input('\n Sweet! Now how long is the width of your rectangle in cm?  ')     #This is asking the user for an input of the width of said rectangle

Area_of_rec = b*c   #this is multiplying the two inputs we got from the user and calling that the area of the rectangle

print "\n Awesome! Your area of your rectangle is %d" % (Area_of_rec)  #printing out the area of the triangle to the user


#this is showing the user that its going to starting asking for inputs to calculate the area of a triangle
print('----------------------------------------------------------\n Now lets find the area of your triangle! \n---------------------------------------------------------- ')

b = input(' Whats the length of the base of your triangle in cm? ')  #this gives the base length of the triangle

h = input(' Whats the height of your triangle in cm? ')  #this gives the hieght of the triangle

Area_of_Tri = 0.5*b*h   #this is the formula to calculate the area of a triangle

print "\n Great!, Your area of your triangle is %d " % (Area_of_Tri) # telling the user what that area of the triangle is



