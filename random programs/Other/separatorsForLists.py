def main():
    myList = []
    cont = 'y'
    while cont.lower() == 'y':
        value = input("enter a number. ")
        try:
            value = float(value)
            myList.append(value)
        except ValueError:
            print("That was not a number.")
        cont = input("Do you want to add another value? ")
    for i in range (0, len(myList)):
        if i >0:
            print (" | ", end="")
        print(myList[i],end="")
    print()
main()
