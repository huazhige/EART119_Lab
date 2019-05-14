circle_radius = 12.6 #sets the circles radius
circle_area = 3.1415*(circle_radius**2) #finds the circles area
a = 1.5
b = 0 #starts at zero
rectangle_area = a * b #sets the height and base multiplied as the area of the rec

while(rectangle_area < circle_area): #while area of rec is less than area of circle it will try next number
	b += 1 #adds one
	rectangle_area = a * b #recalculates the area 
	
print(b) #says area