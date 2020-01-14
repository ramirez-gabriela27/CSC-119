#*******************************************************************
#Program Name:        VandSA.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 22, 2018
#Purpose:             functions to use in VolumeAndSurfacearea.py
#Modules used:        math
#Input Variable(s):   r(float),h(float)
#Output(s):           sphereVol,sphereSA,cylinderVol,cylinderSA,
#                     coneVol,coneSA (all float)
#*******************************************************************

import math

## calculate the volume of a sphere
# @parm r indicating the radius of the sphere
# @return the volume of the sphere as a float
def sphereVolume (r):
    sphereVol = (4/3)*math.pi*(r**3)
    return sphereVol

## calculate the surface area of a sphere
# @parm r indicating the radius of the sphere
# @return the surface area of the sphere as a float
def sphereSurface (r):
    sphereSA = 4*math.pi*(r**2)
    return sphereSA

## calculate the volume of a cylinder
# @parm r indicating the radius of the cylinder
# @parm h indicating the height of the cylinder
# @return the volume of the cylinder as a float
def cylinderVolume(r,h):
    cylinderVol = math.pi*(r**2)*(h)
    return cylinderVol

## calculate the surface area of a cylinder
# @parm r indicating the radius of the cylinder
# @parm h indicating the height of the cylinder
# @return the surface area of the cylinder as a float
def cylinderSurface(r,h):
    cylinderSA = (2*math.pi*r*h)+(2*math.pi*(r**2))
    return cylinderSA

## calculate the volume of a cone
# @parm r indicating the radius of the cone
# @parm h indicating the height of the cone
# @return the volume of the cylinder as a float
def coneVolume(r,h):
    coneVol = math.pi*(r**2)*(h/3)
    return coneVol

## calculate the surface area of a cone
# @parm r indicating the radius of the cone
# @parm h indicating the height of the cone
# @return the surface area of the cone as a float
def coneSurface (r,h):
    coneSA = (math.pi*r)*(r+math.sqrt((h**2)+(r**2)))
    return coneSA
