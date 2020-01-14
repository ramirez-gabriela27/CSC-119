#**************************************************************
#Program Name:        intList.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 29, 2018
#Purpose:             From list of input integers, add them,
#                     find the max and min, and sort the list
#Modules used:        random
#Input Variable(s):   item(int)
#Output(s):           sumList(int),maxList(int),minList(int)
#                     userList(list)
#**************************************************************

def main():
    userList = []
    cont = 'y'
    while cont.lower()=='y':
        try:
            item = int(input("Pleae enter an integer: "))
            userList.append(item)
            cont = input("Would you like to add more? (y/n) ")
        except Exception as myExc:
            print("Something went wrong")
            print("Maybe one of your values was not an integer")
            print("The error was:",myExc)
            cont = input("Do you want to try again?(y/n) ")
    print("\n")
    print("Your list = ",userList)

    #find the sum of all of the input integers
    sumList = sum(userList)
    print("The sum of your list is: ", sumList)
    print("\n")

    #find all extrema on list
    maxList = max(userList)
    minList = min(userList)
    print("The max of your list is: ", maxList)
    print("The min of your list is: ", minList)
    print("\n")

    #sort and print sorted list
    userList.sort()
    print("After sorting")
    print("your list = ",userList)
    print("\n")

main()
input()
