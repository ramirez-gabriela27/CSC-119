#****************************************************************
#Program Name:        countVowels.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 15, 2018
#Purpose:             Find all vowels in a string (a,e,i,o,u)
#                     including all uppercase variants
#Modules used:        None
#Input Variable(s):   string(str)
#Output(s):           vowelNum(int), string(str)
#****************************************************************

def countVowels(string):
    vowels = "aeiouAEIOU"
    vowelNum = 0
    for letter in string:
        if letter in vowels:
            vowelNum += 1
    return vowelNum

def unitTest():    
    #unit test for countVowel(string)
    if countVowels("hello")==2:
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

    #as user for arguments
    string = input("Please input a word: ")
    vowelNum = countVowels(string)
    print("There are ",vowelNum," vowels in the word ",string)

main()
input()
