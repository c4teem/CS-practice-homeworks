# EIGHT

number = int(input())
printed_number = ""
i = 0
while number != 0:
    digit = number % 10
    if digit != 0:
        if number // 10 != 0:
            printed_number += f"{digit * 10**i} + "
        elif number // 10 == 0:
            printed_number += f"{digit * 10**i}"
    i += 1
    number //= 10

print(printed_number)
