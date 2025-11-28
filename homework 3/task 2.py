# TWO

number = int(input())

def func(x):
    if x == 1:
        return 1
    print(x)
    return func(x - 1)
print(func(number))
