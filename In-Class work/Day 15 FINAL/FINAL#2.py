#*******************************************************************
#Program Name:        FINAL#2.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 10 ,2018
#Purpose:             ---
#Modules used:        N/A
#Input Variable(s):   value(float)
#Output(s):           myList,average(float)
#*******************************************************************

## calculate the average of the list
# @param myList - indicates list being added
# @return avg - average
def avg(myList):
    total = 0
    for item in myList:
        total += item
    avg = total/5
    return avg

def main():
    myList = []
    count = 0
    while count < 5:
        value = input("Please enter a number: ")
        try:
            value = float(value)
            myList.append(value)
            count += 1
        #test for ValueError and display if input isn't a number
        except ValueError:
            print("Sorry, you did not input a number, please try again.")
        #test for any other error
        except:
            print("There was an error, please try again.")
    average = round(avg(myList),2)
    print("The avgerage for the list:",myList,"is:",average)

main()
input()
