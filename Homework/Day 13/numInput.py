#************************************************************************
#Program Name:        numInput.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 26,2018
#Purpose:             Have the user input 2 numbers, then divide the
#                     first number by the second, and prints the result
#                     to two decimal places.
#Modules used:        N/A
#Input Variable(s):   num1(float),num2(float)
#Output(s):           numDiv(float)
#************************************************************************

def main():
    cont = 'y'
    while cont.lower() == 'y':
        try:
            num1 = float(input("Please enter a number: "))
            num2 = float(input("Please eneter another number: "))
            numDiv = round(num1/num2,2)
            print(num1,"/",num2,"=",numDiv)
            cont = input("Would you like to do that again?(Y/N)")
        except ValueError as myException:
            print("Your input was not a number, try again.")
            print("The exception was: ",myException)
        except ZeroDivisionError as myException2:
            print("Your second input was zero, try again.")
            print("The exception was: ",myException2)
        except:
            print("There was a different error.")
            print("It was not a ValueError or a ZeroDivisionError")

main()
