#****************************************************************
#Program Name:        extraCredit.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 15, 2018
#Purpose:             Provide a single character from the alphabet
#                     and test it
#Modules used:        None
#Input Variable(s):   character(str)
#Output(s):           vorc(str)
#****************************************************************

def letterType(character):
    #Function tests length of string and if it is a letter
    characterLength = int(len(character))
    if characterLength > 1 or character.isalpha == False:
        vorc = "an invalid character.";
    #if the test is "passed" it recognizes the kind of charachter 
    else:
        vowels = "aeiouAEIOU"
        for letter in character:
            if letter in vowels:
                vorc = "a vowel."
            else:
                vorc = "a consonant."
    return vorc

def main():
    character = input("Please input a character: ")
    vorc = letterType(character)
    print("You input",vorc)

main()
input()
