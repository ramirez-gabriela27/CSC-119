#****************************************************************
#Program Name:        middleString.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 15, 2018
#Purpose:             Return a string containing the middle char.
#                     in string, if string is odd, or 2 middle if
#                     string is even.
#Modules used:        None
#Input Variable(s):   string(str)
#Output(s):           middleChar(str)
#****************************************************************

def middle(string):
    length = int(len(string))
    if length%2 == 1:
        #conditions for string with odd number of characters
        index = int((length/2)+.5)
        middleChar = string[index]
    elif length%2 == 0:
        #conditions for string with even number of characters
        index1 = int((length/2))
        index2 = int((length/2)-1)
        middleChar = string[index1]+string[index2]
    return middleChar

def unitTest():
    #unit test for middle(string)
    if middle("middle")== "dd" and middle("hello")== "l":
        return True
    else:
        return False

def main():
    #unitTest() results
    testPass = unitTest()
    if testPass == True:
        print("Unit Test Passed")
    else:
        print("Unit Test Failed")

    #ask user for arguments
    string = input("Please input a word: ")
    middleChar = middle(string)
    print("Middle character(s):", middleChar)

main()
input()
    
