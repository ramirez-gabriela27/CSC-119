#*********************************************************
#Program Name:        main()function.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Determine if a salary is at or
#                     above the avg US salary, or below
#Modules used:        None
#Input Variable(s):   avgSalary (float)
#Output(s):           Above or below salary 
#*********************************************************

#Determine if a salary is at or above the avg US
#salary, or if is below.

def main():
    avgSalary = 55000.00
    salary = float(input("Input a yearly US salary"))
    if salary >= avgSalary:
        print(salary," is at or above the average.")
    else:
        print(salary," is below the average.")
        
#This is the call to the function main()

main()
