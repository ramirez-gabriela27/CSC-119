import random

def main():
    value = random.randrange(0,20,2)
    print("The random even value = ", value)

    seq = ("Blue","Red","Green","Yellow","Black")
    color = random.choice(seq)
    print ("The random color is: ",color)

main()

