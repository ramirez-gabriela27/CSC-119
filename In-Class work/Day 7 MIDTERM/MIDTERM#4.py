#******************************************************
#Program Name:        MIDTERM#4.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 8, 2018
#Purpose:             Program will count from 1 to 20
#                     and upon reaching 20, it will
#                     count back down to 1.
#Modules used:        None
#Input Variable(s):   None
#Output(s):           value(int), currentValue(int)
#******************************************************

def main():    
    #variable that will change
    currentValue = 20
    #conditional variable
    stopValue = 1
    #to count up, for loop uses range (1,21) to include 20
    for value in range(1,21):
        print (value)
    #to count back down, while loop subtracts from 20 until it reaches 1
    while currentValue>=stopValue:
        print (currentValue)
        currentValue = currentValue-1;

main()

input()
