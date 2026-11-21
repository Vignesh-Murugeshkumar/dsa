
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def kth_largest(arr, k):
    n = len(arr)
    # Index of kth largest in ascending order
    target = n - k
    low = 0
    high = n - 1
    while low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == target:
            return arr[pivot_index]
        elif pivot_index < target:
            low = pivot_index + 1
        else:
            high = pivot_index - 1
    return -1
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k))
