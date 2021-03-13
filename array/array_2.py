'''MAXIMUM AND MINIMUM ELEMENT IN ARRAY'''


def max_min(arr):
    n = len(arr)
    if(n == 0):
        max = []
        min = []
        return max, min
    elif(n == 1):
        max = arr[0]
        min = arr[0]
        return max, min
    elif(n == 2):
        max, min = arr[0], arr[1]
        if(max > min):
            return max, min
        else:
            return min, max
    else:
        max = min = arr[0]
        for i in range(1, n):
            if(max < arr[i]):
                max = arr[i]
            if(min > arr[i]):
                min = arr[i]
    return max, min


arr = [12, 45, 23, 24, 46, 44, 35]
result = max_min(arr)
print("Max = ", result[0], "Min = ", result[1])
