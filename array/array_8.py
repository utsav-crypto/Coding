'''count the triplets'''


def countTriplet(arr, n):
    freq = [0 for i in range(100)]
    for i in range(n):
        freq[arr[i]] += 1
    count = 0

    for i in range(n):
        for j in range(i+1, n, 1):
            if(freq[arr[i]+arr[j]]):
                count += 1
    return count


arr = [1, 1, 1, 2, 2]
n = len(arr)
print(countTriplet(arr, n))
