'''count the triplets'''


def countTriplet(arr, n):
    arr.sort()
    set_a = set(arr)
    max_a = arr[-1]
    c = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            s = arr[i]+arr[j]
            if(s > max_a):
                break
            elif(s in set_a):
                c += 1
    return c


arr = [1, 5, 3, 2]
n = len(arr)
print(countTriplet(arr, n))
