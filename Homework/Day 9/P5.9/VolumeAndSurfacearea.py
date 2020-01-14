#***************************************************************
#Program Name:        VolumeAndSurfacearea.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 22, 2018
#Purpose:             Using an input radius and height
#                     calculate the volume and surface area
#                     of a cone, cylinder, and sphere.
#Modules used:        VandSA
#Input Variable(s):   radius(float),height(float)
#Output(s):           sphereVol,sphereSA,cylinderVol,cylinderSA,
#                     coneVol,coneSA (all float)
#***************************************************************

import VandSA

def main():
    #The user is asked to input a value for r and h
    #to use in the functions being called from VandSA.py
    radius = float(input("Please insert a radius: "))
    height = float(input("Please insert a height: "))

    #The functions are executed with the given inputs
    sphereVol = round(VandSA.sphereVolume(radius),3)
    sphereSA = round(VandSA.sphereSurface(radius),3)
    cylinderVol = round(VandSA.cylinderVolume(radius,height),3)
    cylinderSA = round(VandSA.cylinderSurface(radius,height),3)
    coneVol = round(VandSA.coneVolume(radius,height),3)
    coneSA = round(VandSA.coneSurface(radius,height),3)

    print("\n")
    print("With radius: ",radius,"\n and height: ",height)
    print("\n")
    print("A sphere would have volume ",sphereVol,"and surface area ",sphereSA)
    print("A cylinder would have volume ",cylinderVol,"and surface area ",cylinderSA)
    print("A cone would have volume ",coneVol,"and surface area ",coneSA)

main()
input()
