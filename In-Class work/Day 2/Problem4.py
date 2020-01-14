# R2.3 problem 4
import math
#Variables are created for each variable in equation
a = float(input("a:"))
b = float(input("b:"))
y = float(input("y:"))
#Variables are then used in equation to solve for c
c = math.sqrt((a**2)+(b**2)-((2*a*b)*math.cos(y)))
print("c=",c)

input()
