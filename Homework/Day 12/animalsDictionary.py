#*******************************************************************
#Program Name:        animalsDictionary.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 12,2018
#Purpose:             Determine how many values are 10 and print the
#                     keys for the corresponding values.
#Modules used:        N/A
#Input Variable(s):   N/A
#Output(s):           count(int),key(stg)
#*******************************************************************

def main():
    animals = {"Bird":10,"Dog":15,"Horse":10,"Cat":9,"Mouse":10,"Deer":15}
    print(animals)
    count = 0
    for element in animals:
        if animals[element] == 10:
            count +=1
    print("There are",count,"values equal to 10.")
    print("The following animal types had the value of 10:")
    for element in animals:
        if animals[element] == 10:
            print(element)

main()
input()
