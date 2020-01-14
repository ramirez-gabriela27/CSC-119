def main():
    n = int(input("Please enter a positive, whole, number: "))
    num = 0
    print ("The following numbers are all divisible by 10 within your range:")
    for num in range (1,n+1-10):
        if num %10 == 0:
            print (num)
            num +=1
        else:
            num +=1

main()
