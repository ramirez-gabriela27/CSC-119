#Infinite Loop
#Bad programming with global variable.

# This program is suppose to print out three lines, but
#   there is a typo in the code:
# The value of x is: 0
# the value of x is: 2
x = 0
def incrementX():
    global x
    x = x + 2
    return x

def main():
    global x  # bad programming with global variable.
    # break out of loop when x = 3
    while x != 3:
        print("The value of x is:", x)
        x = incrementX()

main()
    
