#variables
baser = input("The base for the rectangle will be how long? ")
heightr = input("The height for the rectangle will be how long? ")
baset = input("The base for the traingle will be how long? ")
heightt = input("The height for the triangle will be how long? ")

#area functions
area_rectangle = float(baser) * float(heightr)
area_triangle = (float(baset) * float(heightt))/2

# print
print("The area of the rectangle would be " + str(area_rectangle))
print ("The area of the traingle would be " + str(area_triangle))