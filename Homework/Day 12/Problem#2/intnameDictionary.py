#*******************************************************************
#Program Name:        intnameDictionary.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 12,2018
#Purpose:             Write a version of intname.py using a
#                     dictionary
#Modules used:        N/A
#Input Variable(s):   number(int)
#Output(s):           name(stg)
#*******************************************************************

def main() :
   value = int(input("Please enter a positive integer < 1000: "))
   print(intName(value))

## Turns a number into its English name.
#  @param number a positive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def intName(number) :
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number.

   if part >= 100 :
      name = digitName(part // 100) + " hundred"
      part = part % 100

   if part >= 20 :
      name = name + " " + tensName(part)
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0

   if part > 0 :
      name = name + " " + digitName(part)

   return name

## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(digit) :
    digits = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    for element in digits:
        if digit == element:
            value = digits[element]
    return value

## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
def teenName(number) :
    teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    for element in teens:
       if number == element:
           value = teens[element]
    return value

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#
def tensName(number) :
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""

main()
input()
