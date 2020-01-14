#*******************************************************************
#Program Name:        NewStarTheater.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 6,2018
#Purpose:             In a 5x5 grid, print seats and costs
#                     then mark seats sold and display available
#                     to user once selected by row and column
#Modules used:        N/A
#Input Variable(s):   cont(stg), rowInp(int), columnInp(int),
#                     purchase(stg)
#Output(s):           seats(list),seatValue(stg)
#*******************************************************************

def main():
    seats = [
        [" "," "," "," ","Columns"," "," "],
        [" "," ",1,2,3,4,5],
        [" "," "," "," "," "," "," "],
        [" ",1, 50,50,50,50,50],
        [" ",2, 40,45,45,45,40],
        ["Rows",3, 30,35,35,35,30],
        [" ",4, 20,20,20,20,20],
        [" ",5, 10,10,10,10,10]
    ]
    cont = 'y'
    while cont.lower() == 'y':
        rowCount = 8 #seats from 4-8 (3 to 7)
        columnCount = 7 #seats from 3-7 (2 to 6)
        for i in range(rowCount):
            for j in range(columnCount):
                print("%5s"%(seats[i][j]),end="")
            print()
        print()

        #add 2 to input number to find correct row index
        rowInp = 2 + int(input("What row number would you like? "))
        while rowInp<3 or rowInp>7:
            #tested not adjusting for index
            print("The row is not available.")
            print("Please try again.")
            rowInp = 2 + int(input("What row number would you like? "))

        #add 1 to input nuber to find correct column index
        columnInp = 1 + int(input("What column number would you like? "))
        while columnInp<2 or columnInp>6:
            #tested not adjusting for index
            print("The column is not available.")
            print("Please try again.")
            columnInp = 1 + int(input("What column number would you like? "))
        print()

        seatValue = seats[rowInp][columnInp]

        if seatValue == 'SS':
            #'SS' means that the seat has already been sold
            print("This seat has already been sold.")
            print("Please select another seat.")
            cont = 'y'
        else:
            print("You have selected row",rowInp-2,"column",columnInp-1)
            print("This seat's cost is: $",seatValue)
            purchase = input("Would you like to purchase it? (Y/N) ")
            if purchase == 'y':
                seats[rowInp][columnInp] = 'SS'
                print()
                print("You have purchased your seat.")
                print()
            cont = input("Would you like to choose another seat? (Y/N) ")

    if cont.lower() == 'n':
        print()
        print("Sold and unsold seats are displayed below")
        rowCount = 8 #seats from 4-8 (3 to 7)
        columnCount = 7 #seats from 3-7 (2 to 6)
        for i in range(rowCount):
            for j in range(columnCount):
                print("%5s"%(seats[i][j]),end="")
            print()
        print()

main()
input()
