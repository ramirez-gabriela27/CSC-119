#******************************************************
#Program Name:        extraCredit.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 22, 2018
#Purpose:             Calculate the amount of financial
#                     assistance for needy families
#Modules used:        None
#Input Variable(s):   income(float),kids(int)
#Output(s):           aid(float)
#******************************************************

## define if the family can recieve aid based on income and amount of kids
# @parm income indicates the income of the family
# @parm kids indicates the number of kids inthe family
# @return aid indicating the amount of aid the family can/may recieve
def aidAmount (income,kids):
    if income > 30000 and income < 40000 and kids>=3:
        aid = "$1,000 per child"
        return aid
    elif income > 20000 and income < 30000 and kids >=2:
        aid = "$1,500 per child"
        return aid
    elif income <20000 and kids >= 1:
        aid = "$2,000 per child"
        return aid
    else:
        aid = "No aid"
        return aid

def main():
    cont = 'y'
    while cont.lower()=="y":
        try:
            income = float(input("What is your family's income? "))
            kids = int(input("How many children are in the family? "))
            aid = aidAmount(income,kids)
            print("The amount of financial assistance that your family may recieve is \n" ,aid)
            cont = input("Do you want to start over?(Y/N) ")

        except Exception as myExc:
            print("Something went wrong")
            print("Maybe one of your values was not a number")
            print("The error was:",myExc)
            cont = input("Do you want to start over?(Y/N) ")

main()
input()
