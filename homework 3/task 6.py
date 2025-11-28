# SIX

def is_palindrome(x):
    x = x.lower()

    if len(x) <= 1:
        return True

    if x[0] != x[-1]:
        return False

    return is_palindrome(x[1:-1])


word = input()
print(is_palindrome(word))

