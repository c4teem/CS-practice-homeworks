# SEVEN

letters = {'A': 0, 'B': 0, 'C': 0, 
           'D': 0, 'E': 0, 'F': 0,
           'G': 0, 'H': 0, 'I': 0,
           'J': 0, 'K': 0, 'L': 0,
           'M': 0, 'N': 0, 'O': 0,
           'P': 0, 'Q': 0, 'R': 0,
           'S': 0, 'T': 0, 'U': 0,
           'V': 0, 'W': 0, 'X': 0,
           'Y': 0, 'Z': 0}

letter_index = list(letters.keys())

text = input("Enter a text: ")
length1 = len(letter_index)
length2= len(text)

for i in range(length1):
    for j in range(length2):
        if letter_index[i] == text[j].upper():
            letters[letter_index[i]] += 1

max_amount = 0
max_letter = ""

for key, value in letters.items():
    if letters[key] > max_amount:
        max_amount = letters[key]
        max_letter = key

print(f"{max_letter}: {max_amount}")

