def main():
    cost = input("Enter the cost of the item: ")
    if is_float(cost):
        costFloat = float(cost)
        tax = getTax(costFloat)
        totalCost = costFloat+getTax(costFloat)
        print ("The total cost is %5.2f and the tax is %4.2f"\
               %(totalCost,tax))
    else:
        print ("incorrect input")

def is_float (str):
    try:
        float(Str)
        return True
    except ValueError:
        return False
    
def getTax(itemCost):
    if itemCost < 0.0:
        print("The cost of the item must be greater than 0")
        return 0
    else:
        taxRate = .06
        return itemCost*taxRate

main()
