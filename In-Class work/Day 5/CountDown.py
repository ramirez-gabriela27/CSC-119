#*********************************************************
#Program Name:        CountDown.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Understand while loops
#Modules used:        None
#Input Variable(s):   response
#Output(s):           why, oh okay
#*********************************************************

def main():
    print("The while loop example")
    
    #variable that will change
    currentValue = 10
    
    #conditional variable
    stopValue = 0
    
    while currentValue>=stopValue:
        print (currentValue)
        currentValue = currentValue-1;

main()

input()

