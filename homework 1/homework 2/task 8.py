# EIGHT

# IN THIS PART OF CODE WE CREATE A LIST OF WORD AMONG WHICH WE WILL SEARCH AND ARRANGE ANAGRAMS
print('Enter "123" if you want to finish entering the words')
word = input("Enter a word: ")
words_list = []

while word != "123":
    words_list.append(word)
    word = input("Enter a word: ")


# HERE WE CREATE AN ADDITIONAL FUNCTION THAT WOULD HELP US COMPARE IF TWO STRINGS ARE ANAGRAMS
def ordering(the_string) -> list:
    letters = {'A': 0, 'B': 1, 'C': 2, 
           'D': 3, 'E': 4, 'F': 5,
           'G': 6, 'H': 7, 'I': 8,
           'J': 9, 'K': 10, 'L': 11,
           'M': 12, 'N': 13, 'O': 14,
           'P': 15, 'Q': 16, 'R': 17,
           'S': 18, 'T': 19, 'U': 20,
           'V': 21, 'W': 22, 'X': 23,
           'Y': 24, 'Z': 25}
    
    letter_numbers = []
    for i in the_string:
        j = i.upper()
        number = letters[j]
        letter_numbers.append(number)
    return sorted(letter_numbers)


# HERE WE CREATE THE FUNCTION FOR OFERING ANAGRAMS EACH IN ITS OWN GROUP
def anagrams(x) -> list:
    length = len(x)
    returned_list = []

    i = 0
    while i < length:
        j = 0
        the_list = []
        while j < length:
            if ordering(x[i]) == ordering(x[j]):
                the_list.append(x[j])
            j += 1

        if len(the_list) > 1:
            i += len(the_list)
        else:
            i += 1

        returned_list.append(the_list)
    return returned_list

print(anagrams(words_list))
