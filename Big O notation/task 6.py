# The algorithm is O(n²) because for each of the n choices of i, the two-pointer search scans the remaining elements in O(n) time

arr = [1, 3, 4, 7, 11, 20]
target = 25

for i in range(len(arr)):

    left_index = i + 1
    right_index = len(arr) - 1

    while left_index < right_index:
        if arr[left_index] + arr[right_index] + arr[i] == target:
            print(arr[left_index], arr[right_index], arr[i])
            break
        elif arr[left_index] + arr[right_index] + arr[i] < target:
            left_index += 1
        else:
            right_index -= 1
    else:
        print(-1)

