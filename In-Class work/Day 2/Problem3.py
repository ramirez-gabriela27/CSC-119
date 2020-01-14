# R2.3 problem 3
import math
#Variables are created for each variable in equation
a = float(input("a:"))
p = float(input("p:"))
m1 = float(input("m1:"))
m2 = float(input("m2:"))
#Variables are then used in equation to solve for G
g=((4*math.pi)**2)*((a**3)/((p**2)*(m1+m2)))
print("G:",g)

input()
