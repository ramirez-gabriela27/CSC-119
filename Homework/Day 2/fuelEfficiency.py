#calculate the cost of traveling 100 miles with gas prices
print("Please input your car's fuel efficiency (in miles/gallon)")
efficiency = float(input())
print("Please input the current price of gas per gallon")
gas = float(input())
trip=(100*(gas/efficiency))
print("100 mile trip would cost: $",round(trip,2))

input()
