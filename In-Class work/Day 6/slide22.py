def main():
    state = "Colorado is a great state"
    wordCounter = 0
    for letter in state:
        if letter == " ":
            wordCounter +=1
    print ("Number of words in the string =", wordCounter+1)

main()
