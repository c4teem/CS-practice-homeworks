# TEN

number = int(input("Enter a number: "))

array = []

i = 1
while i <= number:
    strings_list = []

    j = 1
    while j <= number:
        string = input("Enter a stirng: ")
        strings_list.append(string)
        j += 1
    
    array.append(strings_list)
    i += 1
    print("\n")
print(array)

def check_vowels(x) -> bool:
    vowels = "AaEeUuIiOo"
    return x[0] in vowels


for i in range(number):
    counting = 0
    for j in range(number):
        if check_vowels(array[j][i]) == True:
            counting += 1
    
    if counting > 2:
        print(f"Column number {i} does not suit the condition")
    else:
        print(f"Column number {i} suits the condition")

