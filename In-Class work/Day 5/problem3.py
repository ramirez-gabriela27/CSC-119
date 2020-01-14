#******************************************************
#Program Name:        problem3.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Use a loop to list numbers from
#                     2 to num and their squares
#Modules used:        None
#Input Variable(s):   num (int)
#Output(s):           num(int), num**2 (int)
#******************************************************

def main():
    num = int(input("Please enter a number between 2 and 20: "))
    #begining value is set to numCurrent
    numCurrent = 2
    #The loop will go from 2 all the way to the inserted number
    while numCurrent <= num:
        numSq = numCurrent**2
        print ("The number=",numCurrent,"and the square of the number=",numSq)
        numCurrent = numCurrent+1;

main()

input()




    
