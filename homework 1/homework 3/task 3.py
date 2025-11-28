# THREE

x, y = int(input("Enter a number: ")), int(input("Enter a power: "))

def powering(x, y):
    if y == 0:
        return 1
    return x * powering(x, y - 1)
print(powering(x, y))


