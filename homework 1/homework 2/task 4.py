# FOUR

the_dict = {}
number = int(input("Enter amount of items you want to add: "))
for i in range(number):
    key = input("Enter key: ")
    value = input("Enter value: ")
    the_dict[key] = value

def reversing_dictionary(d):
    rev_dict = {}
    for key, value in d.items():
        rev_dict[value] = key
    return rev_dict

print(reversing_dictionary(the_dict))
