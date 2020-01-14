#******************************************************************
#Program Name:        vowelCounter.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 1, 2018
#Purpose:             ask user to provide a word and print the ammt
#                     of vowels in the word
#Modules used:        None
#Input Variable(s):   word(string)
#Output(s):           vowelNum (int), word(str)
#******************************************************************

def main():
    vowels = "aeiouy"
    vowelNum = 0
    word = input("Please enter a word: ")
    for letter in word:
        if letter in vowels:
            vowelNum += 1
    print("There are ",vowelNum," vowels in the word ",word)

main()
