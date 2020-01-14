#Find the average of a set of numbers

def main():
    cont = "y"
    total = 0
    while cont.lower()=="y":
        numsEntered = int(input("How many numbers will you enter? "))
        try:
            for i in range(numsEntered):
                num = float(input("input a number "))
                total += num
            aver = total/numsEntered
            print("The average of the numbers is: ",aver)
            cont = input("Do you want to start over?(Y/N)")
        except Exception as myExc:
            print("Something went wrong")
            print("Maybe one of your values was not a number")
            print("The error was:",myExc)
            cont = input("Do you want to start over?(Y/N) ")
main()
