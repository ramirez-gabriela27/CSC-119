#******************************************************
#Program Name:        slide26.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 5,2018
#Purpose:             Manipulate 2D list
#Modules used:        None
#Input Variable(s):   None
#Output(s):           myList
#******************************************************

## squares the values of a given list
# @parm theList indicating the list being squared
# @return sqList
def squares(theList):
    sqList = list(theList)
    for i in range(len(sqList)):
        sqList[i] = sqList[i]*sqList[i]
    return sqList

def main():
    myList = [
        [1,1,1],
        [1,1,1],
        [1,1,1,]
    ]

    #from slide
    for i in range(len(myList[2])):
        myList[2][i] = myList[2][i]+5
    print (myList)

    #changed first row to all zeros
    for i in range(len(myList[0])):
        myList[0][i] = 0
    print(myList)

    #change second row to be [1,2,3]
    x = 0
    for i in range(len(myList[1])):
        x+=1
        myList[1][i] = x
    print(myList)

    #add a fourth row that is [0,1,2]
    newList = [0,1,2]
    myList.append(newList)
    print(myList)

    #add a fifth row that is the squares of row 2
    newList = squares(myList[1])
    myList.append(newList)
    print(myList)

    #print 2D
    row = 5
    column = 3
    for i in range(row):
        for j in range(column):
            print("%10d"%(myList[i][j]),end="")
        print()


main()
