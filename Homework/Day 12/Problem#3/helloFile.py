#*******************************************************************
#Program Name:        helloFile.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 12,2018
#Purpose:             follow tasks on page 444 of Python for Everyone
#                     2nd edition - P7.1
#Modules used:        N/A
#Input Variable(s):   N/A
#Output(s):           message(stg)
#*******************************************************************

def main():
    #open the file to write in
    helloFile = open("hello.txt","w")
    #write message to it
    helloFile.write("Hello,World!")
    #close the file
    helloFile.close()
    #open the file to readline
    message = open("hello.txt","r")
    print(message.read())

main()
