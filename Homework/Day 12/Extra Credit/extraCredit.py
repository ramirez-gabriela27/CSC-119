#*******************************************************************
#Program Name:        extraCredit.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 12,2018
#Purpose:             Page 444 - P7.2
#Modules used:        N/A
#Input Variable(s):   fileIn(stg), fileOut(stg)
#Output(s):           fileOut(txt), filePrint(stg)
#*******************************************************************

def main():
    #ask user for the name of the in/out files
    fileIn = input("Input file name: ")#littleLamb.txt
    fileOut = input("Output file name: ")#littleLamb2.txt

    #open files
    inFile = open(fileIn,'r')
    outFile = open(fileOut,'w')

    #copy file with modifications
    count = 1
    line = inFile.readline()
    while line != "":
        outFile.write("/*")
        outFile.write(str(count))
        outFile.write("*/")
        outFile.write(line)
        count += 1
        line = inFile.readline()
    inFile.close()
    outFile.close()

    #print text of second file
    filePrint = open(fileOut,'r')
    line = filePrint.readline()
    while line != "":
        print(line)
        line = filePrint.readline()
    filePrint.close()

main()
