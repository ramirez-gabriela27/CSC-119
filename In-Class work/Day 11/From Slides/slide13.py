#slide: Day 11 #13

def main():
    myList = [2,4,6,8,10]
    print("The first myList = ",myList)
    squares(myList)
    print("The squared values in myList = ",myList)
def squares(theList):
    for i in range(len(theList)):
        theList[i] = theList[i]*theList[i]
main()
