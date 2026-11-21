def bubbleSortwithEarlyExit(arr):
    n = len(arr)
    for i in range(n):
        swapped = False #early exit flag
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: #if no elements were swapped, the array is already sorted
            break
    return arr