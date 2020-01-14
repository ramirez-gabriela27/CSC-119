def getTax(itemCost):
    taxRate = .06
    return itemCost*taxRate

def main():
    cost = float(input("What is the cost of the item? "))
    tax = getTax(cost)
    totalCost = cost+tax
    print ("The total cost is %5.2f and the tax is %5.2f"\
           %(totalCost,tax))

main()
    
