# The complexity of this code is O(n) due to "for loop"
l = []
x = int(input("Enter the nnumber of elements you want to add: "))
for i in range(x):
    number = int(input())
    l.append(number)

# The complexity of that part is O(n²) because of the "for loop" and removing of items from a list
def f(x):
    length = len(x)
    for i in range(length):
        if x[i] == 0:
            x.append(0)
            del x[i]
    return x

# Overall the code complexity is O(n²)

n = f(l)
print(n)
