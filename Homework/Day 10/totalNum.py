#***********************************************************
#Program Name:        totalNum.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 29, 2018
#Purpose:             Determine the number of items that
#                     are numbers in a list (int and float)
#Modules used:        None
#Input Variable(s):   None
#Output(s):           numInt(int)
#***********************************************************

def main():
    myList = ["Hello","name",6,3.1,7.2,9.4,"Good bye",11.1,22]
    numInt = 0
    for item in myList:
        if(type(item) is int):
            numInt += 1
        elif(type(item) is float):
            numInt +=1
    print ("There are ",numInt," numbers in myList.")

main()
input()
