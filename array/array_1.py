'''REVERSE THE ARRAY'''


def reverse_Array(arr):
    n = len(arr)
    for i in range(n//2+1):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


arr = [12, 45, 23, 24, 46, 44, 35]
print(reverse_Array(arr))
