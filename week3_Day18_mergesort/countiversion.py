def countinversions(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = countinversions(arr[:mid])
    right, right_inv = countinversions(arr[mid:])
    merged, split_inv = merge_and_count(left, right)

    total_inversions = left_inv + right_inv + split_inv
    return merged, total_inversions
def merge_and_count(left, right):
    merged = []
    i = j = inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i  # Count inversions
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
arr=[5, 3, 1, 4, 8, 9, 2, 6, 7]
sorted_arr, inversion_count = countinversions(arr)  
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversion_count)