# FIVE

# Create a function that flattens list of integers ([1, [2, 3, [4]] => [1, 2, 3, 4]) (recursion).

def flatten(x) -> list:
    if x == []: return x
    if type(x[0]) == list:
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])

print(flatten( [1, [2, 3, [4, 5, [6, 7, 8]]]] ))

