# ONE

l = []
x = int(input("Enter the nnumber of elements you want to add: "))
for i in range(x):
    number = int(input())
    l.append(number)

def max_and_min(x):
    maxx = 0
    minn = maxx
    for i in x:
        if maxx < i: maxx = i
    for i in x:
        if minn > i: minn = i
    return f"Maximum: {maxx} and minimum: {minn}"
print(max_and_min(l))
