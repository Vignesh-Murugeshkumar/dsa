def sortedSquares(arr):
    n = len(arr)
    left = 0
    right = n - 1
    result = [0] * n
    pos = n - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] ** 2
            left += 1
        else:
            result[pos] = arr[right] ** 2
            right -= 1

        pos -= 1
    return result
# Main
arr=[-9, -4, -2, 0, 3, 5, 8]

print(sortedSquares(arr))