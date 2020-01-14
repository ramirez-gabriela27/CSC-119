#***********************************************************
#Program Name:        randomList.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 6,2018
#Purpose:             Create a list of random values
#                     and find the sum, average, extrema
#                     and sort it.
#Modules used:        random
#Input Variable(s):   N/A
#Output(s):           sum(int),avg(int),max(int),min(int)
#                     randomList
#***********************************************************

## finds the avg of the list of values
# @parm myList indicating the list form which the avg is found
# @return avg
def average(myList):
    avg = sum(myList)/len(myList)
    return avg

def main():
    import random
    myList = []
    for i in range(25):
        value = random.randint(1,100)
        myList.append(value)

    print(myList)
    print()
    print("The sum of the list = ",sum(myList))
    avg = average(myList)
    print("The avergae value in the list = ",avg)
    print("The max of the list = ",max(myList))
    print("The min of the list = ",min(myList))
    print()
    myList.sort()
    print("The sorted list = ",myList)

main()
