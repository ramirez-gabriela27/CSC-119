#***********************************************************
#Program Name:        studentClass.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 17, 2018
#Purpose:             Determine a student's class status
#                     based on the amount of credits they
#                     have taken
#Modules used:        None
#Input Variable(s):   Cred (int)
#Output(s):           Print student statues (string)
#***********************************************************

#freshman 0 - 23
#sophomore 24-48
#junior 49 - 72
#senior >72

cred = int(input("Please enter the amount of credits you have taken: "))

if cred>0 and cred <=23:
    print ("you are a Freshman.")
elif cred>=24 and cred<=48:
    print ("you are a Sophomore.")
elif cred>=49 and cred<=72:
    print ("you are a Junior.")
else:
    print ("you are a Senior.")

input()
