def main():
    num = 0
    total = 0

    while num <=100:
        if num %2 == 0:
            total = total+num
            num += 1
        else:
            num +=1
    print("The sum of all even numbers between 0 and 100 is: ",total)

main()
