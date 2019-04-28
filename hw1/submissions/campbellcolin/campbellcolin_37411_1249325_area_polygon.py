# input variables
x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5, 4]
summa = 0

for i in range(0, 5):
    number = (0.5*((x[i-1]*y[i])- (y[i-1]*x[i])))
    summa = summa + number
    print("The current number is: " + str(number))
print("The area is: " + str(summa))