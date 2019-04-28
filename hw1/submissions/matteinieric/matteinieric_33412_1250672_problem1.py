"""
Homework 1 problem 1
Area of a rectangle A = b*c
Area of a triangle A = 0.5*h*b
"""
# to have user put in values, use below function
# float( raw_input("what are your initial savings?"))
b = float( raw_input("What is the length of the base?"))
c = float(raw_input("Height of rectangle?"))
h = float(raw_input("height of triangle?"))
A_R = b*c
A_T = 0.5 * h * b

print("length of base (b) = %f " %(b))
print("height of rectangle (c) = %f" %(c))
print("height of triangle (h) = %f" %(h))

print("rectangle area =%f"%(A_R))
print("triangle area =%f"%(A_T))
