#*******************************************************************
#Program Name:        FINAL#3.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 10 ,2018
#Purpose:             create a list of 40 random numbers [1,15]
#                     then find the sum.
#Modules used:        random
#Input Variable(s):   N/A
#Output(s):           myList,total(int)
#*******************************************************************

import random

def main():
    count = 0
    myList = []
    total = 0
    #create list of random values
    while count < 40:
        value = random.randint(1,15)
        myList.append(value)
        count += 1
    #add numbers in list
    for item in myList:
        total += item
    print("The total sum of the list:",myList,"is:",total)

main()
input()
