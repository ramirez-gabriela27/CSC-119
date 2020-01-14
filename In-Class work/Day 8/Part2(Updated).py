#**************************************************************
#Program Name:        P5.1Part2.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 15, 2018
#Purpose:             Write a program to find the smallest num,
#                     and avg. of 3 input nums.
#Modules used:        None
#Input Variable(s):   x,y,z (all floats)
#Output(s):           testPassMin(str),testPassAvg(str),
#                     minimum (float), average(float)
#**************************************************************


#for minimum and minimum test**********************************
def smallest(x,y,z):
    minimum = 1000000000
    if x < minimum:
        minimum = x
    elif y < minimum:
        minimum = y
    elif z < minimum:
        minimum = z
    return minimum

def UnitTestMin():
    if smallest(1,2,6) == 1 :
        return True
    else:
        return False
#**************************************************************

#for average and average test**********************************
def average(x,y,z):
    total = x+y+z
    avg = total/3
    return avg

def UnitTestAvg():
    if average(1,2,6) == 3:
        return True
    else:
        return False
#**************************************************************

def main():
    #UnitTestMin() results
    passMin = UnitTestMin()
    if passMin == True:
        print("Unit Test Passed(smallest)")
    else:
        print("Unit Test Failed(smallest)")
    #UnitTestAvg() results
    passAvg = UnitTestAvg()
    if passAvg == True:
        print("Unit Test Passed(average)")
    else:
        print("Unit Test Failed(average)")
        
    #ask user for arguments
    print("Please enter 3 numbers")
    x = float(input())
    y = float(input())
    z = float(input())
    #call smallest and average functions and display results
    minimum = smallest(x,y,z)
    print("The minimum value entered is: ", minimum)
    avg = average(x,y,z)
    print("The average of the values entered is: ",avg)

main()
input()





