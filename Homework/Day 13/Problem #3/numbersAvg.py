#************************************************************************
#Program Name:        numbersAvg.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 26,2018
#Purpose:             Find the avg of the numbers in 2 columns of a csv
#                     file
#Modules used:        csv
#Input Variable(s):   numbersAvg.csv
#Output(s):           column1Avg(float), column2Avg(float)
#************************************************************************

def main():
    from csv import reader
    inFile = open("numbersAvg.csv","r")
    count = 0
    total = 0
    numList = reader(inFile)

    #colum 1
    for row in numList:
        total = total + float(row[0])
        count = count + 1
    column1Avg = total/count
    print("The average of the numbers in the first column = %5.3f"%(column1Avg))

    #column 2
    total2 = 0
    count2 = 0
    for row in numList:
        total2 = total2 + float(row[1])
        count2 = count2 + 1
    column2Avg = total2/count2
    print("The average of the numbers in the second column = %5.3f"%(column2Avg))

main()
