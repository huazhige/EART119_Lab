#Problem 3
import math                         #Allows pi to be used

a = 1.5                             #One side of the rectangle in millimeters

r = 12.6                            #Radius of the circle

def area_r(a,b):                    #Defining the area of the rectangle
    area_r = a*b                    #The formula for the area of the rectangle
    return area_r                   #Allows area_r to be used again

area_c = (math.pi)*r**2             #The formula for the area of the circle

b = 0                               #b starts at 0 in the while loop

while area_r(a, b) <= area_c:       #Finding b while the area of the rectangle 
                                        #is less than the area of the cirlce
    b += 1                          #The loop is adding one to b each time it 
                                        #runs until it gets to the correct area

print(b-1)                          #Must be b-1 because b alone prints a 
                                        #number that creates a higher rectangle
                                        #area than the circle area