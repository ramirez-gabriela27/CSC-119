def main():
    onceMore = 'y'
    animals = {'cow':4,'horse':6,'goat':3,'dog':2}

    while onceMore =='y':
        theAnimal = input("What animal are you looking for? ")
        theAnimal = theAnimal.lower()
        value = animals.get(theAnimal,"no animals")
        print("There are ",value," animals of the type ",theAnimal)
        onceMore = input("Do tou want to continue:(y)or(n)? ")
main()
