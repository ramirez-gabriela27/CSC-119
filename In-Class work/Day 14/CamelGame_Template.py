#****************************************************
# program:          CamelGame.py
# prgrammer:        
# date:             
# updated:           
# Purpose:          A text game with a camel going across
#                   the Mobi desert.
# Required Modules: random
# Inputs:           letter choices
# Outputs:          Text messages
# Updates:
#
#*****************************************************
import random
def quit():
    print("I am guitting now.")
    return True

def status(milesTraveled, thirst, camelTiredness, distanceNativesTraveled, drinks):
    print("Need to do the code")
    
def main():
    choice = ""
    done = False  # loop variable

    #variables for game
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    distanceNativesTraveled = -20
    drinks = 5


    while not done:
        print(
        """
        Welcome to the Camel Game?
        You have stolen a camel to make your way across the great Mobi desert.
        The natives want their camel back and are chasing you down?  Survive your
        desert trek and out run the native.

        A - Drink from you canteen.
        B - Ahead moderate speed. 
        C - Ahead full speed. 
        D - Stop and rest for night.
        E - Status check.
        Q - Quit the Game
        """
        )

        choice = input(" Your  choice?\n")
        if choice.upper() == "Q":
            done = quit()
    
        elif choice.upper() == "B":
            pass
        elif choice.upper() == "A":
            pass
        elif choice.upper() == "B":
            pass
        elif choice.upper() == "C":
            pass
        elif choice.upper() == "D":
            pass
        elif choice.upper() == "E":
            pass
              
        else:
            print("That was not a correct choice - Enter (A through E or Q)")
        
        
# call main
main()



