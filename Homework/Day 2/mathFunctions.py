#ask user for three inputs
print("Please input 3 numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())
import math
#finds the max of the function
numMax = max(num1,num2,num3)
print("The maximum value is:",numMax)
#finds the min of the function
numMin = min(num1,num2,num3)
print("The minimum value is:",numMin)
#finds the absolute value of the first input
numAbs = abs(num1)
print("The absolute value of the first input is:",numAbs)
#finds the sqrt of the largest
numSqr = float(math.sqrt(numMax))
print("The square root of the largest number is:",numSqr)

input()
