#******************************************************
#Program Name:        volumeSphere.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Oct 22, 2018
#Purpose:             calculate the volume of the sphere
#                     with input radius
#Modules used:        areas
#Input Variable(s):   radius(float),cont(strg)
#Output(s):           volumeS(float)
#******************************************************
import areas

def main():
    cont = 'y'
    while cont.lower()=="y":
        try:
            radius = float(input("Please input the radius of the sphere "))
            volumeS = areas.volumeSphere(radius)
            print("The volume of the sphere is ",volumeS)
            cont = input("Do you want to start over?(Y/N)")
        except Exception as myExc:
            print("Something went wrong")
            print("Maybe one of your values was not a number")
            print("The error was:",myExc)
            cont = input("Do you want to start over?(Y/N) ")

main()
input()
