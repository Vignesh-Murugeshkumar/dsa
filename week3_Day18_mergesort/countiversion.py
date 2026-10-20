def merge(left, right):
    result = [0] * (len(left) + len(right)) #initialize result array with zeros
    i = j = k = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            count += len(left) - i
            j += 1
        k += 1
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1
    return result, count


def countInversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2 
    left, c1 = countInversions(arr[:mid])#left half of the array
    right, c2 = countInversions(arr[mid:])#right half of the array
    merged, c3 = merge(left, right)
    return merged, c1 + c2 + c3

arr = [5, 3, 2, 4, 1]
sorted_arr, count = countInversions(arr)
print("Sorted array:", sorted_arr)
print("Count:", count)