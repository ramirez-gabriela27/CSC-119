def main():
    #Prompt the user for the name of the input+output files
    inputFileName = input("Input file name: ")
    outputFileName = input("Output file name: ")

    #Open the input and output files
    infile = open(inputFileName, "r")
    outfile = open(outputFileName, "w")

    #read the input and write the output
    total = 0.0
    count = 0

    line = infile.readline()
    while line != "":
        value = float(line)
        outfile.write("%15.2f\n"%value)
        total = total+value
        count = count+1
        line = infile.readline()
    outfile.write("%15s\n"%"--------")
    outfile.write("Total: %8.2f\n"%total)
    avg = total/count
    outfile.write("Average: %6.2f\n"%avg)

    infile.close()
    outfile.close()
main()
