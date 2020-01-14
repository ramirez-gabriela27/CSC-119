def main():
    seats = [] # initialize the theater seats
    file = open("TheaterCosts.txt", "r")
    lines = []
    # read all the lines at once into the lines list.
    lines = file.readlines()
    file.close()  # done with the file

    # populate the seats List.
    row = 5     # five rows
    column = 5 # five columns in each row
    # read a single line in from the List created above called "lines".
    for singleLine in lines:
        singleLine.strip() # get rid of the "\n"
        # re-create a one dimensial list each time through the loop with split().
        itemsInList = singleLine.split()
        #Fill seats from intemInList to the row needed
        theRow = []  # initilize the inner row - used to append to seats.
        for i in range(column):
            #Convert seat to a float.
            try:
                item = float(itemsInList[i])
            except ValueError:
                print("That was not a number")
            theRow.append(item)
        seats.append(theRow)    # append the inner row to the 2D seats List.
    # You now have a 2D List of seat prices.
    # Now print the seats 2D List.
    for i in range(row):
        for j in range(column):
            print("%10d"%(seats[i][j]), end="")
        print()
main()
