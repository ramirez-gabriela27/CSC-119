#********************************************************
#Program Name:        WaterStates.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Sept 17, 2018
#Purpose:             Determine the state of water
#                     based on the temperature of water
#Modules used:        None
#Input Variable(s):   temp (float) , degrees (string)
#Output(s):           print state of water
#********************************************************

#Solid at 32 F or 0 C
#Gas at 212 F or 100 C
#Liquid in between

temp = float(input ("Please input the temperature: "))
degrees = input ("Are you using Fahrenheit (F) or Celsius (C) ? ")

if degrees == "C":
    if temp<=0:
        print ("The water is solid")
    elif temp>100:
        print ("The water is gas")
    else:
        print ("The water is liquid")

if degrees == "F":
    if temp<=32:
        print ("The water is solid")
    elif temp > 212:
        print ("The water is gas")
    else:
        print ("The water is liquid")

input()
