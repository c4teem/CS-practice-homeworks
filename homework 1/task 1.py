# ONE

maximum = 0
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    maximum = n1
else:
    maximum = n2
if n2 > n3:
    maximum = n2
else:
    maximum = n3
print(maximum)
