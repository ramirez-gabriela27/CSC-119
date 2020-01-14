#in cm (2.54 cm in an inch)
#program that displays the perimeter of (8.5*11in) paper
#as well as the length of the diagonal

widthIn = float(8.5)
lengthIn = float(11)

widthCm = widthIn * float(2.54)
lengthCm = lengthIn * float(2.54)

import math 
perimeter = (widthCm*2)+(lengthCm*2)
diagonal = math.sqrt((widthCm**2)+(lengthCm**2))

print("an 8.5in*11in sheet of paper has a perimeter of:"\
      ,perimeter , "cm")
print("and a diagonal of:", round(diagonal,2) , "cm") 

input()
