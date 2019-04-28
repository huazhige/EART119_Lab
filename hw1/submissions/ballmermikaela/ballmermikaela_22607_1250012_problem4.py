#Problem 4

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Part A
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math                                 #Allows e to be used
from math import e

"""
No = initial amount of the substance
t = change in time
T = half-life
N = quantity of the substance
"""

t = 2                                       #imputting random numbers for the 
T = 2                                           #variables
No = 2

def generic_calculator(No, t, T):           #defining
    N = (No)*(e)**(-t/T)                    #N = quantity of the substance
    return N
print('With a given initial amount, N = ' + str(generic_calculator(No, t, T)))
                                            #printing N
t = 2                                       #imputting random numbers for the
T = 2                                           #variables
#No = not given

def generic_calculator2(t, T):              #defining N/No
    N_divided_by_No = (e)**(-t/T)           #N = quantity of the substance
    return N_divided_by_No
print('Without a given initial amount, N/No = ' + str(generic_calculator2(t, T)))
                                            #printing N/No

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Part B
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

T = 5730                                    #half life of carbon 14

No = input("Initial amount of substance = ")#asking the user to input initial
                                                #amount

def remaining_amount(T,No):                 #finding the remaining amount
                                                #of the substance
    amount_after_10kyr = (No)*(e)**(-(10000)/T)     #after 10k years
    amount_after_100kyr = (No)*(e)**(-(100000)/T)   #after 100k years
    amount_after_1Myr = (No)*(e)**(-(1000000)/T)    #ater 1 million years
    print(amount_after_10kyr/No)
    print(amount_after_100kyr/No)
    print(amount_after_1Myr/No)
    

remaining_amount(T,No)                      #calling the function

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Part C
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

t = input("Change in time = ")              #asking the user for variables
T = input("Half-life = ")
No = input("Initial amount (if this amount is not known, write 'None')= ")

def generic_calculator(No, t, T):
    N = (No)*(e)**(-t/T)                    #N = quantity of the substance
    return N

if No == None:                              #what to print if No is not given
    print("N/No = "+ str((e)**(-t/T)))
else:                                       #what to print if No is given
    amount_left = generic_calculator(No, t, T)
    print("Amount left = "+ str(amount_left))
