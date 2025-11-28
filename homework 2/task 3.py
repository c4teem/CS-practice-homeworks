# THREE

x = int(input("Enter the amount of numbers you want to add: "))
l = []

for i in range(x):
    number = int(input(f"Enter a number: "))
    l.append(number)

def reversing(x):
    reversed_l = []
    f = len(x)
    for i in range(f):
        reversed_l.append(x[f - 1])
        f -= 1
    return reversed_l
print(reversing(l))
