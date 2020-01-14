#*************************************************************
#Program Name:        extraCredit.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 24, 2018
#Purpose:             Program is meant to simulate a bank acc.
#Modules used:        None
#Input Variable(s):   savingsAmt (float), checkingAmt (float)
#Output(s):           savingsAmt (float), checkingAmt (float)
#*************************************************************

def main():
    #Input amount in Savings account and make sure it is positive
    savingsAmt = float(input("Please enter the amount in your savings account: \n"))
    if savingsAmt < 0:
        print("Negative balance not accepted")
        savingsAmt = float(input("Please try again: \n"))
    #Input amount in Checking account and make sure it is positive
    checkingAmt = float(input("Please enter the amount in your checking account: \n"))
    if checkingAmt < 0:
        print("Negative balance not accepted")
        checkingAmt = float(input("Please try again: \n"))

    selectionChoice = input("What kind of transaction?(deposit, withdrawal, or transfer): \n")

    #For deposit
    if selectionChoice == "deposit":
        selectionAccount = input("In which account? (savings or checking): \n")
        depositAmt = float(input("How much do you want to deposit? \n"))
        if selectionAccount == "savings" :
            savingsAmt = savingsAmt+depositAmt
        elif selectionAccount == "checking" :
            checkingAmt = checkingAmt+depositAmt
        else:
            print("Invalid Transaction \n")
    #For withdrawal
    elif selectionChoice == "withdrawal":
        selectionAccount = input("In which account? (savings or checking): \n")
        withdrawalAmt = float(input("How much do you want to withdrawal? \n"))
        if selectionAccount == "savings":
            if withdrawalAmt>savingsAmt:
                print("Insufficient funds \n")
            else:
                savingsAmt = savingsAmt-withdrawalAmt
        elif selectionAccount == "checking":
            if withdrawalAmt>checkingAmt:
                print("Insufficient funds \n")
            else:
                savingsAmt = savingsAmt-withdrawalAmt
        else:
            print("Invalid Transaction \n")
    #For transfer
    elif selectionChoice == "transfer":
        selectionAccount = input("In which account? (savings or checking): \n")
        transferAmt = float(input("How much do you want to transfer? \n"))
        if selectionAccount == "savings" :
            if transferAmt>savingsAmt:
                print("Insufficient funds \n")
            else:
                savingsAmt = savingsAmt-transferAmt
                checkingAmt = checkingAmt+transferAmt
        elif selecitonAccount == "checking":
            if transferAmt>checkingAmt:
                print("Insufficient funds \n")
            else:
                checkingAmt = checkingAmt-transferAmt
                savingsAmt = savingsAmt+transferAmt
    else:
        print("Invalid Transaction \n")

    #Format and print amounts in accounts
    savingsSt = "Your Savings balance is:  $"
    checkingSt = "Your Checking balance is: $"
    print("%s%0.2f"%(savingsSt, savingsAmt))
    print("%s%0.2f"%(checkingSt, checkingAmt))


main()

input()
