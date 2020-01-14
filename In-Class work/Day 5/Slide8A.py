
# Determine if a salary is above, below or
# at the average US salary

def main():
    try:
        salary = float(input("Input a yearly US salary") )
        if salary >avgSalary:
            print(salary, " is above the average.") 
        elif salary < avgSalary:
            print(salary, " is below the average.") 
        else:
            print(salary, " is at the average.")
    except:
        print("What you entered is not a number")
    
main()      

