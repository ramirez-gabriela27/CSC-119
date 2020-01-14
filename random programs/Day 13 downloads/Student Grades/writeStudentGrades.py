import csv
def main():
    outfile = open("grades.csv","w", newline="")
    csvWriter = csv.writer(outfile, lineterminator='\n')
    name1 = "Mary"
    grade1 = 95
    name2  = "Joe"
    grade2 = 87
    name3 = "Sam"
    grade3 = 97
    # must use a list to write
    csvWriter.writerow( ["Name","Grade"] )
    csvWriter.writerow( [name1,grade1])
    csvWriter.writerow( [name2,grade2] )
    csvWriter.writerow( [name3,grade3] )
    outfile.close()
main()
