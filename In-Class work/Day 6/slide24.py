def main():
    vowels = "aeiou"
    word = input("What is the word? ")
    for letter in word:
        if letter in vowels:
            print("The",letter,"is a vowel in the word",word)
main()
