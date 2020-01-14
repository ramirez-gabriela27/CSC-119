#translate pseudocode into Python
#bookstore computes the price of an order from the total price and amount

print("Please insert the number of books ordered:")
numBooks = int(input())
print("Please insert the price of the book:")
priceBook = float(input())

#calculates the total cost using the guidelines in the pseudocode
totalpriceBook = priceBook*numBooks
tax = totalpriceBook*.075
shipcharge = 2*numBooks
totalCost = round(totalpriceBook+tax+shipcharge,2)

print ("The price of the order is: $",totalCost)

input()
