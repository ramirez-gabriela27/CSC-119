#******************************************************
#Program Name:        seasons.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 17, 2018
#Purpose:             Determine the season the user is
#                     in by month and day inserted.
#                     (using pseudo code)
#Modules used:        None
#Input Variable(s):   month (int), day(int), season
#Output(s):           Seasons (Witner, Spring, Summer,
#                     or Fall)
#******************************************************

month = int( input("Please insert the month (as number): "))
day = int( input("Please insert the day (as number): "))
season = input()

#First, identify season from month
if month==1 or month==2 or month==3:
    season = "Winter"
if month==4 or month==5 or month==6:
    season = "Spring"
if month==7 or month==8 or month==9:
    season = "Summer"
if month==10 or month==11 or month==12:
    season = "Fall"

#Next, identify it by day
if month %3==0 and day>=21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"

print ("The season is: ", season)

input()
