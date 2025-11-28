# SIX

binary_number = int(input())
i = 0
number = 0
while binary_number != 0:
    number += (binary_number % 10) * 2**i
    i += 1
    binary_number //= 10
    
print(number)