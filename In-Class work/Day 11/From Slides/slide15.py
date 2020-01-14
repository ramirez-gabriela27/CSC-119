#slide: Day 11 #15

def main():
    myList = [72.5,69.2,85.9,93.7,77.8]
    print("myList = ",myList)
    averageQuiz = quiz_average(myList)
    print("The average minus the lowest grade is: %4.1f" %averageQuiz)

def quiz_average(theList):
    myList = list(theList)
    myList.remove(min(myList))
    averageValue = sum(myList)/len(myList)
    print("List without lowest score: ",myList)
    return averageValue

main()
