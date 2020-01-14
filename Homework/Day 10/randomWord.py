#***********************************************************
#Program Name:        randomWord.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 29, 2018
#Purpose:             From list of input words, pick a
#                     random one when user no longer wants
#                     to input an item
#Modules used:        random
#Input Variable(s):   item(string)
#Output(s):           randomItem (string)
#***********************************************************
import random

def main():
    insertList = []
    cont = 'y'
    while cont.lower()=='y':
        item = input("Pleae enter a word: ")
        insertList.append(item)
        cont = input("Would you like to add more? (y/n) ")
    print ("your list = ",insertList,"\n")
    randomItem = random.choice(insertList)
    print("Random word form your list: ",randomItem)

main()
input()
