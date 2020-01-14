#*******************************************************************
#Program Name:        Problem#1.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 26,2018
#Purpose:             Slide 12 of ppt for Day 13
#Modules used:        N/A
#Input Variable(s):   wordList2.txt, string(stg)
#Output(s):           myDictionary
#*******************************************************************

def main():
    file = open("wordList2.txt","r")

    myDictionary = {}
    string = "input the first thing that comes to mind when I say:"
    for line in file:
        word = line.strip()
        value = input(string.strip() + word + ":")
        if word not in myDictionary:
            myDictionary[word]=value
    print(myDictionary)
    file.close()

main()
