#*******************************************************************
#Program Name:        FINAL#1.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 10 ,2018
#Purpose:             Have the user input a number and test if it's
#                     even or odd. Test for ValueError.
#Modules used:        N/A
#Input Variable(s):   num(int),cont(stg)
#Output(s):           num(int)
#*******************************************************************

def main():
    cont = 'y'
    while cont.lower() == 'y':
        try:
            num = int(input("Please enter a number: "))
            numKind = num%2
            if numKind == 1:
                print("The number:",num,"is odd")
            else:
                print("The number:",num,"is even")
            cont = input("Would you like to try again? (y/n)")
        #test for ValueError and display if input isn't a number
        except ValueError:
            print("Sorry, you did not input a number, please try again.")
        #test for any other error
        except:
            print("There was an error, please try again.")

main()
input()
