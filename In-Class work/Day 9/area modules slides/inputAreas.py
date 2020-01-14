#inputAreas.py

import areas
def main():
    radius = float(input("What is the radius of the cricle? "))
    areaCir = areas.areaOfCircle(radius)
    print("The are of the circle of radius",radius,"is",areaCir)

    width = float(input("What is the width of the rectangle? "))
    length = float(input("What is the length of the rectangle? "))
    areaRect = areas.areaOfRectangle(width,length)
    print("The are of the rectangle is", areaRect)

main()
input()
