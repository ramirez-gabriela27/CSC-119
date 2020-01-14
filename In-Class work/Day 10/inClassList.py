#In class list practice
#Day 10 *** Gabriela Tolosa Ramirez **** Oct 29, 2018

def main():
    myList = [1,10,20,21,5,7,9,13,10,20,55]

    # 1.) Find the length of the list
    sizeMyList = len(myList)
    print("From myList: ", myList)
    print("The size of myList is: ", sizeMyList)
    print("\n")

    # 2.) Find the sum of all the numbers in the list
    sumMyList = sum(myList)
    print("The sum of myList is: ", sumMyList)
    print("\n")

    # 3.) Find the max and the index of the max
    maxMyList = max(myList)
    indexMax = myList.index(maxMyList)
    print("The Largest value of myList is: ",maxMyList)
    print("The max is located in Index ",indexMax)
    print("\n")

    # 4.) Test values in loop to find 21 and its index
    for index in range(0,len(myList)):
        value = myList[index]
        if value == 21:
            print("The value IS     21 at index: ",index)
        else:
            print("The value is not 21 at index: ",index)
    print("\n")

    # 5.) Change all 10's to 15's
    print("From myList: ", myList)
    for index in range(0,len(myList)):
        value = myList[index]
        if value == 10:
            myList[index] = 15
    print("After changing 10's to 15's")
    print("myList =",myList)
    print("\n")

    # 6.) creating new list, concatonate together with myList and put new in
    # front of old, but call it myList too
    newList = [20,8]
    myList = myList + newList
    print("After adding newList")
    print("myList =",myList)
    print("\n")

    # 7.) append() - add a 12 to end of list
    print("From myList: ", myList)
    myList.append(12)
    print("After appending 12")
    print("myList =",myList)
    print("\n")

    # 8.) insert() - add a 16 to front of list
    print("From myList: ", myList)
    myList.insert(0,16)
    print("After inserting 16")
    print("myList =",myList)
    print("\n")

    #9.) sort the list
    myList.sort()
    print("After sorting")
    print("myList =",myList)
    print("\n")

    # 10.) pop() - delete last item in the list, print the deleted item
    # and the new list
    print("From myList: ", myList)
    item = myList.pop(len(myList)-1)
    print("After deleting last item: ",item)
    print("myList =",myList)
    print("\n")

    # 11.) Count how many twenties there are and print the count
    count = 0
    for value in myList:
        if value == 20:
            count += 1
    print ("There are ", count, "20's in myList")
    print("\n")

    # 12.) remove() - delete the first 20 from list
    myList.remove(20)
    print("After remving the first 20")
    print("myList =",myList)
    print("\n")

    print("After all of the changes,")
    print("myList = ", myList)

main()
input()
