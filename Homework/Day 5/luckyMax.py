#******************************************************
#Program Name:        luckyMax.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Determine how many years Max can
#                     spend $54,000 a year (startin at
#                     year 0 and amount $1M) 
#Modules used:        None
#Input Variable(s):   n/a
#Output(s):           years (int)
#******************************************************

def main():
    #local variables are defined
    currentAmt = 1000000
    years = 0
    stopAmt = 0

    #conditions are set to stop the loop for as long as the amount is greater than 0
    while currentAmt >= stopAmt:
        currentAmt = currentAmt-54000
        years = years+1

    #compensate for the fact that year 0 is essentally year 1 when printing result
    print("Max can withdraw $54,000 for",years-1,"years before he can't withdraw $54,000 a year")

main()

input()
