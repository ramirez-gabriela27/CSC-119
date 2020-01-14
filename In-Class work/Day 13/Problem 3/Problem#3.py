#*******************************************************************
#Program Name:        Problem#3.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 26,2018
#Purpose:             Slide 21&22 of ppt for Day 13
#Modules used:        csv
#Input Variable(s):   name(stg),grade(stg)
#Output(s):           stidentGrades.csv
#*******************************************************************

import csv

def main():
    outfile = open("studentGrades.csv","w", newline="")
    csvWriter = csv.writer(outfile,lineterminator="\n")

    cont = 'y'
    csvWriter.writerow(["Name","Grade"])

    while cont.lower() == 'y':
        name = input("Name: ")
        grade = input("Grade: ")
        csvWriter.writerow([name,grade])

        cont = input("Would you like to continue?(N/Y) ")

main()
