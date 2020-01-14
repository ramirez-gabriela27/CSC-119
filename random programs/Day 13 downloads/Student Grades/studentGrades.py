# studentGrades.py
# Author    Helena
# Date      March 23, 2016

# import the csv
def main():
    from csv import reader
    total = 0
    count = 0
    INFILE = open("studentGrades.csv","r")
    gradeList = reader(INFILE)
    for row in gradeList:
        total = total + float(row[1])
        count = count + 1
    average = total/count
    print ("The class average is:%5.2f"%(average))
    INFILE.close()
main()
