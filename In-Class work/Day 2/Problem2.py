# R2.3 problem 2
#Variables are created for each variable in equation
PV = float(input("Present Value:"))
INT = float(input("Interest:"))
YRS = float(input("Years:"))
#Variables are then used in equation to solve for Final Value
FV = PV*(1+(INT/100))**YRS
print("Final Value:",round(FV,2))

input()
