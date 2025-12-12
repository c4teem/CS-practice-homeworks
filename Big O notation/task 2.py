# The complexity of this code is O(n) due to "for loop"
l = []
x = int(input("Enter the nnumber of elements you want to add: "))
for i in range(x):
    number = int(input())
    l.append(number)

# Time complexity: O(n) because the two-pointer technique moves each pointer at most n steps.
def f(x, target):
    length = len(x) - 1

    l_index = 0
    r_index = length

    while l_index < r_index:
        if x[l_index] + x[r_index] == target:
            return x[l_index], x[r_index]
        elif x[l_index] + x[r_index] < target:
            l_index += 1
        elif x[l_index] + x[r_index] > target:
            r_index -= 1
    
    return -1

# Overall the code complexity is O(n)

n = f(l, 6)
print(n)