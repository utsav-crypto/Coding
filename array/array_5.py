'''Move -ve element to one side of an array'''


def sort(arr):
    low = high = 0
    for i in range(len(arr)):
        if(arr[i] < 0):
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high += 1
        else:
            high += 1
    return arr


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(sort(arr))
