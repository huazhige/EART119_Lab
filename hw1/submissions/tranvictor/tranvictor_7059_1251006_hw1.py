import math

def prob_one():
    b=input("Enter breadth of Rectangle: ") #input for breadth of rectangle
    l=input("Enter length of Rectangle: ") #input for length of rectangle
    c=input("Enter the c for triangle: ") #input for c of triangle
    length=int(l) #take input from user
    breadth=int(b)
    cccc=int(c)
    arearec=length*breadth #formula for area of rectangle
    areatri=.5*breadth*cccc #formula for area of triangle
    print("Area of Rectangle =",arearec)
    print("Area of Triangle =",areatri)

def poly(xVector,yVector):
    eq1 = xVector[0] * yVector[1] + xVector[1] * yVector[2] + xVector[2] * yVector[3]+ xVector[3] * yVector[4]+ xVector[4] * yVector[0]
    #using array as forumla
    eq2 = yVector[0] * xVector[1] + yVector[1] * xVector[2] + yVector[2] * xVector[3]+ yVector[3] * xVector[4]+ yVector[4] * xVector[0]
    sum = .5 * (eq1 - eq2) #using results from above to finish equation
    return sum

def poly_for(x,y):
    a = 0
    for i in range(0,len(x)): #iterating through both arrays
        # print(i)
        if i < len(x)-1:
            det = (x[i]*y[i+1])-(y[i]*x[i+1]) #while not at last indice do equation
        else:
            det = (x[i]*y[0])-(x[0]*y[i]) #for last indice do first times last
        a+=det
    a = abs(a)/2 #take absolute value and divide by 2
    print(a)

def prob_three():
    r = 12.6
    a = 1.5
    circle_area = math.pi * (r*r) #use math formula and pi from math library
    rectangle_area = 0
    goal_b = 0; #declaring variable for greatest width
    while (rectangle_area < circle_area): #increase goal width until rectangle area is greater than the circle area
        goal_b+=0.1
        rectangle_area = goal_b*a #recalculating with new value
    goal_b-=0.1 #subtract by one value to get last value that created an area less than the circle
    print(goal_b)

def bonus(time, half_life, initial=None):
    t = time/half_life #define t
    if initial is not None: #if no intital value is given
        return initial * (math.pow(0.5,t)) #return final value
    else:
        return math.pow(0.5,t) #return exponent

def bonus_b():
    ten_thousand = bonus(10000,5730) #use given value 10,000
    hun_thousand = bonus(100000, 5730) #use given value 100,000
    mil = bonus(1000000, 5730) #use given value 1,000,000
    return ten_thousand, hun_thousand, mil #return given values

def bonus_c():
    t = input("elapsed time: ") #get user input
    l = input("half-life: ") #get user input
    return bonus(float(t),float(l)) #return values with floating point accuracy

def main(): #main function to run all parts of the program
    x = [1,3,4,3.5,2]
    y = [1,1,2,5,4]
    prob_one()
    print(poly(x,y))
    poly_for(x,y)
    prob_three()
    print(bonus(7.2,2.4,100))
    print(bonus(7.2,2.4))
    print(bonus_b())
    print(bonus_c())