#******************************************************
#Program Name:        MIDTERM#3.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 8, 2018
#Purpose:             Roll a die 4 times, and find the
#                     average of 4 rolls.
#Modules used:        Random
#Input Variable(s):   None
#Output(s):           avg(float)
#******************************************************

import random

def main():
    total = 0
    #initiate loop with range from 1 to 5 (in order to "roll" 4 times)
    for x in range (1,5):
        roll = random.randint(1,6)
        total +=roll
    #average is found by adding all of the values of rolls and div. by 4    
    avg = total/4
    #Displays the average and rounds it to 2 decimal places
    print ("The average of the 4 rolls is ", round(avg,2))

main()

input()
