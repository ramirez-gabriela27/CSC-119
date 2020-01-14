#******************************************************
#Program Name:        tempConvert.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 15, 2018
#Purpose:             Convert temperature form Celsius
#                     to Fahrenheit and vise versa
#Modules used:        None
#Input Variable(s):   onceMore(str),tempType(str),
#                     cValue(float),fValue(float)
#Output(s):           cValue(float),fValue(float)
#******************************************************

def cToF (temp):
    f = ((9.0/5.0)*temp)+32
    return f

def fToC (temp):
    c = (temp-32)*5.0/9.0
    return c

def main():
    onceMore = 'y'
    while onceMore.lower() == 'y':
        tempType = input("What temperature are you converting into (f or c)? ")

        if tempType.lower() == "f":
            cValue = float(input("What is the temperature in Celsius? "))
            fValue = cToF (cValue)
            print("The Fahrenheit value is:",fValue,"and the Celsius calue is: ",cValue)
        elif tempType.lower() == "c":
            fValue = float(input("What is the temperature in Fahrenheit? "))
            cValue = fToC (fValue)
            print("The Celsius value is:",cValue,"and the Fahrenheit calue is:",fValue)
        else:
           print("You did not anser with a 'f' or 'c'")
        onceMore = input("Do you want to continue(y/n)? ")

main()
input()
