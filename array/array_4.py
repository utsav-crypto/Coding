'''Sort the array which consists of only 0, 1 and 2 without any sorting algorithm'''


def sort(arr):
    low = mid = 0
    high = len(arr)-1
    while(mid <= high):
        if(arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif(arr[mid] == 1):
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


arr = [0, 1, 1, 2, 0, 0, 1, 2, 0, 1, 2]
print(sort(arr))
