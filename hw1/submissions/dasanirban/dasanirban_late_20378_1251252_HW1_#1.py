def computeArea(b,c,h):
  print "The area of the rectangle is "+str(b*c)+"."
  print "The area of the triangle is "+str(b*h)+"."

computeArea(3,4,5)

#another way to do the same thing
def computeArea2(b,c,h,s):
  if s=="rectangle":
    return b*c
  if s=="triangle":
    return b*h

print computeArea2(3,4,5,"rectangle")
print computeArea2(3,4,5,"triangle")
