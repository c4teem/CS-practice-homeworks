# NINE

n = int(input("Enter: ")) + 1

def factors_sum(x) -> int:
    summs = [0]
    fact = 1
    for i in range(1, n):
        fact *= i
        summs.append(fact + summs[-1])
    return summs[-1]
        

print(factors_sum(n))
