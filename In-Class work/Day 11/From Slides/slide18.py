#slide: Day 11 #18

def main():
    import random
    myList = []
    for i in range(10):
        value = random.randint(1,100)
        myList.append(value)
    print(myList)
    print("The sum of the list = ",sum(myList))

main()
