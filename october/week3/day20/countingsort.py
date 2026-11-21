def countsort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    # Initialize the count array with zeros
    count = [0] * (max_val + 1) 
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    # Build the sorted output array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
arr = [4, 2, 2, 8, 3, 3, 1]
print(countsort(arr))