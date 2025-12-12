# The complexity of the code it O(n)

l = [8, 1, 2, 2, 1, 6, 8]

result = 0
for i in l:
    result ^= i

print(result)