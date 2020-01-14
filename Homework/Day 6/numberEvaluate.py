#******************************************************************
#Program Name:        numberEvaluate.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 1, 2018
#Purpose:             as user to input values and evaluate
#                     average, minimum, maximum and the range
#Modules used:        None
#Input Variable(s):   listAmt(int),
#Output(s):           listMax,listMin,listRange,listAvg
#******************************************************************

def main():
    listAmt = int(input("How many values are in your list? (more than 3) "))
    total = 0
    listMax = -1000000000000
    listMin = 1000000000000
    for x in range(1,listAmt+1):
        print("Enter value #" +str(x))
        num=float(input())
        total = total+num
        if listMax < num:
            listMax=num
        if listMin > num:
            listMin=num
    print("The max is: ", listMax)
    print("The min is: ", listMin)
    listRange = listMax-listMin
    print("The range is: ", listRange)
    listAvg = total/listAmt
    print("The avergae is: %.2f "%(listAvg))


main()
