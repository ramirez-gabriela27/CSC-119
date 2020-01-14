#*******************************************************************************
#Program Name:        camelGame.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 3,2018
#Purpose:             A text game with a camel going across
#                     the Mobi desert.
#Modules used:        random
#Input Variable(s):   letter choices (stg)
#Output(s):           text messages (stg)
#Updates:
#*******************************************************************************

import random

## makes the user drink (A)
# @param drinks
# @return drinks
def userThirst(drinks):
    if drinks > 0:
        drinks = drinks - 1
        thirst = 0
        print("You have taken a drink from your canteen.")
        return drinks
    else:
        print("You are out of water!")

## takes camel ahead at a moderate speed (B)
# @param thirst,camelTiredness,milesTraveled
# @return thirst,camelTiredness,milesTraveled
def aheadModerate(thirst,camelTiredness,milesTraveled):
    thirst = thirst + 1
    camelTiredness = camelTiredness + 1
    miles = random.randint(5,12)
    milesTraveled = milesTraveled + miles
    return (thirst,camelTiredness,milesTraveled)

## takes camel ahead at full speed (C)
# @param thirst,camelTiredness,milesTraveled
# @return thirst,camelTiredness,milesTraveled
def aheadFull(thirst,camelTiredness,milesTraveled):
    thirst += 1
    camelTiredness = camelTiredness + random.randint(1, 3)
    miles = random.randint(10,20)
    milesTraveled = milesTraveled + miles
    return (thirst,camelTiredness,milesTraveled)

## takes break for night (D)
# @param camelTiredness
# @return camelTiredness
def rest(camelTiredness):
    camelTiredness = 0
    print("You have rested for the night")
    print("The camel is happy.")
    return camelTiredness

## gives the user a status report (E)
# @param milesTraveled, thirst, camelTiredness, distanceNativesTraveled, drinks
# @return status report in print statements
def status(milesTraveled, thirst, camelTiredness, distanceNativesBehind, drinks):
    print("Miles traveled : ",milesTraveled)
    if thirst > 4:
        print("Your thirst : ",thirst)
        print("You are thirsty.")
    else:
        print("Your thirst : ",thirst)
    if camelTiredness > 6:
        print("Camel Tiredness : ",camelTiredness)
        print("Your camel is tired")
    else:
        print("Camel Tiredness : ",camelTiredness)
    print("Drinks in canteen : ",drinks)
    print("The natives are ",distanceNativesBehind," miles behind you")

## exit the game (Q)
# @param N/A
# @return True
def quit():
    print("I am guitting the game now.")
    return True

## calculate the distance traveled by natives
# @param milesTraveled, thirst, camelTiredness, distanceNativesTraveled, drinks
# @return status report in print statements
def nativesTraveled(distanceNativesBehind,milesTraveled):
    distance = random.randint(7, 14)
    distanceNativesBehind = milesTraveled - (-distanceNativesBehind+distance)
    return distanceNativesBehind

def main():
    choice = ""
    done = False  # loop variable

    #variables for game
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    distanceNativesBehind = 20
    drinks = 5

    print(
    """
    Welcome to the Camel Game!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down!  Survive your
    desert trek and out run the native.
    """
    )
    while done == False:
        print(
        """
        A - Drink from you canteen.
        B - Ahead moderate speed.
        C - Ahead full speed.
        D - Stop and rest for night.
        E - Status check.
        Q - Quit the Game
        """
        )
        findOasis = random.randint(1,20)
        choice = input(" Your  choice?\n")

        #display game conditions if needed
        if thirst > 4:
            print("You are thirsty")
        if camelTiredness > 5:
            print("Your camel is tired")

        # found oasis!!
        elif findOasis is 1 :
            print("Wow! You've found an Oasis! Your canteen is full, your camel is happy, and you are no longer thirsty")
            drinks = 5
            thirst = 0
            camelTiredness = 0

        # take a drink
        elif choice.upper() == 'A':
            #test for game conditions
            if thirst > 6:
                print("Game over : You died of thirst.")
                quit()
            elif camelTiredness > 8:
                print("Game over : Your camel got too tired.")
                quit()
            elif distanceNativesBehind == 0:
                print("Game over : The natives cought you.")
                quit()
            else:
                drinks = userThirst(drinks)
                distanceNativesBehind = nativesTraveled(distanceNativesBehind,milesTraveled)

        # travel at a moderate speed
        elif choice.upper() == "B":
            #test for game conditions
            if thirst > 6:
                print("Game over : You died of thirst.")
                quit()
            elif camelTiredness > 8:
                print("Game over : Your camel got too tired.")
                quit()
            elif distanceNativesBehind == 0:
                print("Game over : The natives cought you.")
                quit()
            else:
                thirst,camelTiredness,milesTraveled = aheadModerate(thirst,camelTiredness,milesTraveled)
                distanceNativesBehind = nativesTraveled(distanceNativesBehind,milesTraveled)
                print("You have traveled at a moderate speed.")
                if milesTraveled == 200:
                    print("You have won the game!")
                    quit()

        # travel at full speed
        elif choice.upper() == "C":
            #test for game conditions
            if thirst > 6:
                print("Game over : You died of thirst.")
                quit()
            elif camelTiredness > 8:
                print("Game over : Your camel got too tired.")
                quit()
            elif distanceNativesBehind == 0:
                print("Game over : The natives cought you.")
                quit()
            else:
                thirst,camelTiredness,milesTraveled = aheadFull(thirst,camelTiredness,milesTraveled)
                distanceNativesBehind = nativesTraveled(distanceNativesBehind,milesTraveled)
                print("You have traveled at full speed.")
                if milesTraveled == 200:
                    print("You have won the game!")
                    quit()

        # stop and rest for the night
        elif choice.upper() == "D":
            #test for game conditions
            if thirst > 6:
                print("Game over : You died of thirst.")
                quit()
            elif distanceNativesBehind == 0:
                print("Game over : The natives cought you.")
                quit()
            else:
                camelTiredness = rest(camelTiredness)
                distanceNativesBehind = nativesTraveled(distanceNativesBehind,milesTraveled)

        #gives you a status report
        elif choice.upper() == "E":
            status(milesTraveled, thirst, camelTiredness, distanceNativesBehind, drinks)

        #quits the game
        elif choice.upper() == "Q":
            done = quit()

        #the user didn't enter a proper choice
        else:
            print("That was not a correct choice - Enter (A through E or Q)")

# call main
main()
input()
