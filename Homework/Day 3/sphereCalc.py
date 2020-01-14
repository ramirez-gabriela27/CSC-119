#prompts the user for a radius
print("Please insert a radius:")
radius = float(input())

#calculates and prints the area and circumference of circle
import math
area = math.pi*radius**2
circum = math.pi*radius*2

print("The area is:", round(area,2))
print("The circumference is:" , round(circum,2))

#calculates volume and surface area of a sphere with same radius
volume = (4/3)*math.pi*radius**3
surfaceA = 4*math.pi*radius**2
print("\n")
print("A sphere with the same radius would have")
print("Volume:" , round(volume, 2))
print("Surface area", round (surfaceA, 2))

input()
