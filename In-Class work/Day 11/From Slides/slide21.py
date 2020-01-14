#slide: Day 11 #21

def main():
    row = 3
    column = 4
    grades = [
        [97,64,81,75],
        [88,65,91,83],
        [75,93,72,81]
    ]
    print(grades)
    print()
    for i in range(row):
        for j in range(column):
            print("%10d"%(grades[i][j]),end="")
        print()
main()
