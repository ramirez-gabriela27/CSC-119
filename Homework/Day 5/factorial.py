#******************************************************
#Program Name:        factorial.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             User must input a number and the
#                     program will find the factorial
#                     value of the number
#Modules used:        None
#Input Variable(s):   number (int)
#Output(s):           result (int)
#******************************************************

def main():
    #Variable for the input number and the start number are created
    number = int(input("Please enter a number: "))
    numStart = 1
    numFactorial = numStart
    #condition will go from 1 to the number input
    while numStart <= number:
        #loop for factorial function
        numFactorial = numFactorial*numStart
        numStart = numStart+1
    print (number,"! (factorial) is equal to = ", numFactorial)

#call the main function
main()

input()
