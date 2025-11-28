# SIX

amount = int(input("Enter amount of strings you want to add: "))
strings = []

for i in range(amount):
    string = input("Enter a string: ")
    strings.append(string)
print(strings)

unique_strings = []
for i in range(len(strings)):
    count = 0
    for j in range(len(strings)):
        if strings[i] == strings[j] and i != j:
            count += 1
    if count == 0 and len(strings[i]) > 5:
        unique_strings.append(strings[i])

print(unique_strings)

