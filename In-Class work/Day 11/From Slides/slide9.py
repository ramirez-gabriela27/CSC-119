#slide: Day 11 #9

def main():
    myList = []
    cont = 'y'
    while cont.lower() == 'y':
        value = input("enter a number. ")
        try:
            value = float(value)
            myList.append(value)
        except ValueError:
            print("That was not a number. ")
        cont = input("Do you want to add another value? ")
    print(myList)
    try:
        string1 = "What is the first index you want to swap? The last index is " \
        + str(len(myList)-1) + ":"
        string2 = "What is the second index you want to swap? The last index is " \
        + str(len(myList)-1) + ":"
        swap1 = int(input(string1))
        swap2 = int(input(string2))
    except ValueError:
        print("You did not enter an integer.")

    temp = myList[swap1]
    myList[swap1] = myList[swap2]
    myList[swap2] = temp
    print(myList)

main()
