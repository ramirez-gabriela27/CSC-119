#slide16
def showGrade(person="Marty", grade='F'):
    print("The student", person,"has a grade of",grade)
def main():
    name = input("Enter a Name ")
    inGrade = input("Enter a Grade ")
    #This print the default name and grade.
    showGrade()
    #This prints the input name and grade.
    showGrade(grade=inGrade, person=name)
    #This prints the default name but the input grade.
    showGrade(grade=inGrade);
main()
