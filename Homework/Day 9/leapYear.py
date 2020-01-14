#******************************************************
#Program Name:        leapYear.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 22, 2018
#Purpose:             Determine if a year is a leap year
#                     based on the user input year
#Modules used:        None
#Input Variable(s):   year(int)
#Output(s):           leapYear(stg)
#******************************************************

## define if the input year is a leap year
# @parm year indicates the year being tested
# @return leapYear
def isLeapYear(year):
    #a year of 366 is a leap year
    #divisable by 4, or 400 but not 100
    if year < 1582:
        leapYear = "is outside of domain"
        return leapYear
    elif year%400 == 0 and year > 1582:
        leapYear = "is a leap year"
        return leapYear
    elif year%4 == 0 and year > 1582:
        leapYear = "is a leap year"
        return leapYear
    else:
        leapYear = "is not a leap year"
        return leapYear

def main():
    try:
        year = int(input("Please enter a year(after 1582): "))
        leapYear = isLeapYear(year)
        print("The year ", year, leapYear)
    except Exception as myExc:
        print("Something went wrong")
        print("Maybe one of your values was not a number")
        print("The error was:",myExc)

main()
input()
