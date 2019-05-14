import numpy

#variables
quantity = input("What is the initial amount of material? If unknown press 0. ")
halflife = float(input("What is the half life of the material? "))
time = float(input("How much time has elapsed?  "))

#function
if quantity == 0:
    amount = (float(quantity))*(numpy.exp(-time/halflife))
    amount = numpy.exp(-time/halflife)
    print("This means that " + str(amount*100) + "% of the material remains after " + str(time) + " years.")
else:
    amount = (float(quantity))*(numpy.exp(-time/halflife))
    print("After " + str(time) + " years there is " + str(amount))
    print("This means that " + str((amount/float(quantity))*100) + "% of the material remains after " + str(time) + " years.")