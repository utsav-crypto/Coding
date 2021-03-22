'''union and intersection of two sorted array'''


def union_intersection(arr1, arr2):
    arr3 = []
    for element in arr2:
        if element not in arr1:
            arr1.append(element)
        elif element in arr1:
            arr3.append(element)
    return arr1, arr3


arr1 = [12, 43, 25, 37, 20]
arr2 = [43, 28, 19, 12, 56]
union, intersection = union_intersection(arr1, arr2)

print("Union = ", union, "Intersection = ", intersection)
