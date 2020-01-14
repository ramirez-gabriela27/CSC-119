#areas.py

import math

## calculate the are of a circle
# @parm radius indicating the radius of the circle
# @return the area of the circle as a float
def areaOfCircle(radius):
    areaS = math.pi*radius**2
    return areaS

## calculate the are of a rectangle
# @parm width indicating the width of the rectangle
# @return the area of the rectangle as a float
def areaOfRectangle(width,length):
    areaR = length*width
    return areaR

## calculate the volume of a sphere
# @parm radius indicating the radius of the sphere
# @return the volume of the sphere as a float
def volumeSphere (radius):
    volumeS = (4/3)*math.pi*(radius**2)
    return volumeS

