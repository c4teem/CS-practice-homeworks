# FIVE

number = int(input("Enter the amount of items you want to add: "))
the_dict = {}
for i in range(number):
    key = input("Enter key: ")
    value = input("Enter value: ")
    the_dict[key] = value

def update(x, dictionary):
    for key, value in dictionary.items():
        x[key] = value
    return x

second_dict = {"age": 18, "name": "Azat"}
print(update(the_dict, second_dict))