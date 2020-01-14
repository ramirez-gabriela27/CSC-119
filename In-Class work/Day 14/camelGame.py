#*******************************************************************
#Program Name:        camelGame.py
#Programmer:          Gabriela Tolosa Ramirez, Henry Ordonez
#CSC - 119:           Fall 2018 - 002
#Date:                Dec 3,2018
#Purpose:             A text game with a camel going across
#                     the Mobi desert.
#Modules used:        random
#Input Variable(s):   letter choices (stg)
#Output(s):           text messages (stg)
#Updates:
#*******************************************************************

import random

## makes the user drink (A)
# @param user input
# @return userThirst value to 0
def userThirst(drinks):
    drinks = drinks - 1
    thirst = 0
    return drinks

## takes camel ahead at a moderate speed (B)
# @param thirst,camelTiredness,milesTraveled
# @return milesTraveled
def aheadModerate(thirst,camelTiredness,milesTraveled):
    thirst = thirst + 1
    camelTiredness = camelTiredness + 1
    miles = random.randint(5,12)
    milesTraveled = milesTraveled + miles
    return (thirst,camelTiredness,milesTraveled)

## takes camel ahead at full speed (C)
# @param thirst,camelTiredness,milesTraveled
# @return milesTraveled
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
    return camelTiredness

## gives the user a status report (E)
# @param user input
# @return status report in print statements
def status(milesTraveled, thirst, camelTiredness, distanceNativesTraveled, drinks):
    print("Miles traveled : ",milesTraveled)
    print("Drinks in canteen : ",drinks)
    print("The natives are ",distanceNativesTraveled," miles behind you")

## exit the game (Q)
# @param user input
# @return True
def quit():
    print("You are guitting the game now.")
    return True

## calculates distance traveled by natives
# @param distanceNativesTraveled, milesTraveled
# @return diffTravel
def nativesTraveled(distanceNativesTraveled, milesTraveled):
    distance = random.randint(7, 14)
    distanceNativesTraveled = distanceNativesTraveled + distance
    diffTravel = milesTraveled - distanceNativesTraveled
    return diffTravel


def main():
    choice = ""
    done = False  # loop variable

    #variables for game
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    distanceNativesTraveled = -20
    drinks = 5

    print(
    """
    Welcome to the Camel Game!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the native.
    """
    )

    while not done:
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
        #set choice to user input
        choice = input(" Your  choice?\n")

        #quit
        if choice.upper() == "Q":
            done = quit()

        #drink from canteen
        elif choice.upper() == "A":
            if thirst > 4:
                print("You are thirsty")
                userThirst(drinks)
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            print("You have drank from canteen.")
            if camelTiredness > 5:
                print("Your camel is thirsty")
                userThirst(drinks)
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            print("You have drank from canteen.")
            if distanceNativesTraveled >= 0:
                print("The natives caught up, You are dead.")
                quit()
            if thirst> 6:
                print("You are too thirsty, You are dead.")
                quit()
            if camelTiredness>8:
                print("Your camel is too tired, You are dead.")
                quit()

        #ahead moderate speed
        elif choice.upper() == "B":
            if thirst > 4:
                print("You are thirsty")
                thirst,camelTiredness,milesTraveled = aheadModerate(thirst,camelTiredness,milesTraveled)
                print("you have traveled ",milesTraveled," miles.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if camelTiredness > 5:
                print("Your camel is thirsty")
                thirst,camelTiredness,milesTraveled = aheadModerate(thirst,camelTiredness,milesTraveled)
                print("you have traveled ",milesTraveled," miles.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if distanceNativesTraveled >= 0:
                print("The natives caught up, You are dead.")
                quit()
            if thirst> 6:
                print("You are too thirsty, You are dead.")
                quit()
            if camelTiredness>8:
                print("Your camel is too tired, You are dead.")
                quit()

        #ahead full speed
        elif choice.upper() == "C":
            if thirst > 4:
                print("You are thirsty")
                thirst,camelTiredness,milesTraveled = aheadFull(thirst,camelTiredness,milesTraveled)
                print("you have traveled ",milesTraveled," miles.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if camelTiredness > 5:
                print("Your camel is thirsty")
                thirst,camelTiredness,milesTraveled = aheadFull(thirst,camelTiredness,milesTraveled)
                print("you have traveled ",milesTraveled," miles.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if distanceNativesTraveled >= 0:
                print("The natives caught up, You are dead.")
                quit()
            if thirst> 6:
                print("You are too thirsty, You are dead.")
                quit()
            if camelTiredness>8:
                print("Your camel is too tired, You are dead.")
                quit()

        #stop and rest for night
        elif choice.upper() == "D":
            if thirst > 4:
                print("You are thirsty")
                camelTiredness = rest(camelTiredness)
                print("You have rested for the night and the camel is happy.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if camelTiredness > 5:
                print("Your camel is thirsty")
                camelTiredness = rest(camelTiredness)
                print("You have rested for the night and the camel is happy.")
                distanceNativesTraveled = nativesTraveled(distanceNativesTraveled, milesTraveled)
            if distanceNativesTraveled >= 0:
                print("The natives caught up, You are dead.")
                quit()
            if thirst> 6:
                print("You are too thirsty, You are dead.")
                quit()
            if camelTiredness>8:
                print("Your camel is too tired, You are dead.")
                quit()

        #status report
        elif choice.upper() == "E":
            status(milesTraveled, thirst, camelTiredness, distanceNativesTraveled, drinks)

        else:
            print("That was not a correct choice - Enter (A through E or Q)")
# call main
main()
