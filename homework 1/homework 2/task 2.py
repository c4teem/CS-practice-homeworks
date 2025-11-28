# TWO

string = input("Enter a string: ")

def unique_letters(s):
    l = set()
    for i in string: l.add(i)
    return l
print(unique_letters(string))
