# SEVEN

the_list = []

print("Enter a word 'stop' to stop entering: ")
word = input("Enter: ")

while word != "stop":
    the_list.append(word)
    word = input("Enter a word: ")

def find_element(x, y):
    try:
        return x[y]
    except IndexError:
        return None

print(f"\n{find_element(the_list, 10)}")

