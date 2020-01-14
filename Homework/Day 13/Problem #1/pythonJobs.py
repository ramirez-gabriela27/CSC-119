#*******************************************************************
#Program Name:        pythonJobs.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 26 ,2018
#Purpose:             Print out the avg. yearly salary and the avg.
#                     number of years of experience.
#Modules used:        csv
#Input Variable(s):   pythonJobs.csv
#Output(s):           avgSalary(float),avgExp(float)
#*******************************************************************

def main():
    from csv import reader
    INFILE = open("pythonJobs.csv","r")
    jobList = reader(INFILE)

    #to find average salary
    total = 0
    totalExp = 0
    count = 0
    avgSalary = 0 #column 2
    for row in jobList:
        total = total + float(row[2])
        totalExp = totalExp + float(row[3])
        count += 1

    avgSalary = total/count
    print("The average salary is : $%5.2f"%(avgSalary))
    avgExp = totalExp/count
    print("The average years of experience needed is : %5.2f"%(avgExp) , "years")

main()
