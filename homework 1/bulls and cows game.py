# BULLS AND COWS GAME

origin_number = input("Enter the 4 digit number to play bulls and cows game: ")
while len(origin_number) != 4:
    print("\nENTER ONLY 4 DIGITS!!!!!!!")
    origin_number = input("Enter the number to play bulls and cows game: ")


guess_number = input("\nGuess the 4 digit number: ")
while len(guess_number) != 4:
    print("\nENTER ONLY 4 DIGITS!!!!!!!")
    guess_number = input("Guess the number: ")

bulls = 0
cows = 0

for i in range(4):
    for j in range(4):
        if guess_number[i] == origin_number[j] and i == j:
            bulls += 1
        elif guess_number[i] == origin_number[j] and i != j:
            cows += 1
if bulls == 4:
    print("IT'S A WIN WIN!!!")
else:
    print(f"{bulls} bulls and {cows} cows")

    while guess_number != origin_number:
        bulls = 0
        cows = 0

        guess_number = input("\nGuess the 4 digit number: ")
        while len(guess_number) != 4:
            print("\nENTER ONLY 4 DIGITS!!!!!!!")
            guess_number = input("Guess the number: ")

        for i in range(4):
            for j in range(4):
                if guess_number[i] == origin_number[j] and i == j:
                    bulls += 1
                elif guess_number[i] == origin_number[j] and i != j:
                    cows += 1
        if bulls == 4:
            print("IT'S A WIN WIN!!!")
        else:
            print(f"{bulls} bulls and {cows} cows")