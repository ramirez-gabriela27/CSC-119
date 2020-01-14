#************************************************************************
#Program Name:        FINAL#4.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 10 ,2018
#Purpose:             Read the csv file and find the sum, min and max
#Modules used:        csv
#Input Variable(s):   test.csv
#Output(s):           sum(float),minNum(float),maxNum(float)
#************************************************************************

def main():
    #open and read the file
    inFile = open("test.csv")
    from csv import reader
    csvReader = reader(inFile)
    #make a list
    myList = []
    for row in csvReader:
        value = float(row[0])
        myList.append(value)
    #calculate the average
    count = 0
    total = 0
    for item in myList:
        total = total+float(item)
        count = count+1
    average = total/count
    print("The average = ",average)
    #find max
    maxNum = max(myList)
    print("The max = ",maxNum)
    #find min
    minNum = min(myList)
    print("The min = ",minNum)

    inFile.close()

main()
input()
