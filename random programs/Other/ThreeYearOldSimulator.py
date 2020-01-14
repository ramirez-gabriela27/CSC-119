#*********************************************************
#Program Name:        ThreeYearOldSimulator.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Understand while loops
#Modules used:        None
#Input Variable(s):   response
#Output(s):           why, oh okay
#*********************************************************

def main():
    print("The sky is Blue.\n")
    #This is the Sentry Variable
    response = " "
    while response != "Because.":
        response = input("Why?\n")
        print (response)
    print ("Oh. Okay.")

main()

