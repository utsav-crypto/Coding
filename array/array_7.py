'''find subarray with given sum'''


def subarray(arr, n, s):
    for i in range(n):
        cur_sum = arr[i]
        j = i+1
        while(j <= n):
            if cur_sum == s:
                print("found between", i, "and", j-1)
            if cur_sum > s or j == n:
                break
            cur_sum += j
            j += 1
    print("not found")
    return -1


arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
s = 17
subarray(arr, n, s)
