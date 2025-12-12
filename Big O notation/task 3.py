# The complexity of this code is O(n) due to "for loop"
l = []
x = int(input("Enter the nnumber of elements you want to add: "))
for i in range(x):
    number = int(input())
    l.append(number)

# The complexity of the code is O(n) due to working with the list
def max_profit(x):
    min_price = x[0]
    maximum_profit = 0

    for price in x:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > maximum_profit:
                maximum_profit = profit
    
    return maximum_profit

# Overall the complexity is O(n)

n = max_profit(l)
print(n)