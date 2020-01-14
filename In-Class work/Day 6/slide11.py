def main():
    value = "Y"    
    while value == "Y" or value== "y":
        num1= float(input("Please enter a number: "))
        num2= float(input("Please enter a scond number: "))
        num3= float(input("Please enter a third number: "))

        average = (num1+num2+num3)/3
        print ("The average of the three numbers is: ", average)

        value = input("Do you want to do this again?(Y/N)")

main()
