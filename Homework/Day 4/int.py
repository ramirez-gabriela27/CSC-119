#******************************************************
#Program Name:        int.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 17, 2018
#Purpose:             Read an integer and determine if
#                     it is +, -, or 0
#Modules used:        None
#Input Variable(s):   num (int)
#Output(s):           Print (pos, neg, 0)
#******************************************************

num = int( input("Please enter a number: "))

if num==0:
    print ("The number is 0.")
if num<0:
    print ("The number is negative.")
if num>0:
    print ("The number is positive.")

input()
