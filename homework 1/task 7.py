# SEVEN

number = int(input())
i = 0
binary_number = 0

while number != 0:
    digit = number % 2
    binary_number += digit * 10**i
    i += 1
    number //= 2

print(binary_number)
