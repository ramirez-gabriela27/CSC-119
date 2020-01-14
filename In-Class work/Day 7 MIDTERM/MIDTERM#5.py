#******************************************************
#Program Name:        MIDTERM#5.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 8, 2018
#Purpose:             Add up odd numbers form 0 to 300.
#Modules used:        None
#Input Variable(s):   None
#Output(s):           total (int)
#******************************************************

def main():
    num=0
    total=0
    #loop is using range from 0 to 301(to include 300)
    for x in range(0,301):
        #if num is divisible by 2 and has remainder 1
        if num %2 == 1:
            total = total+num
            num += 1
        else:
            num +=1
    print("The sum of all odd numbers between 1 and 300 is: ",total)

main()

input()
