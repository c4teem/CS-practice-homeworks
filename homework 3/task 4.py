# FOUR

length = int(input("Enter the length: "))

def fibonacci(x):
    sequence = [1, 1]
    while x > 2:
        sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])
        x -= 1
    return sequence

print(fibonacci(length))
print(len(fibonacci(length)))
