def sortcolor(arr):
    count = [0] * 3  
    # Count the occurrences of each color
    for color in arr:
        count[color] += 1
    # Reconstruct the sorted array based on the counts
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            arr[index] = color
            index += 1
    return arr
arr = [2, 0, 2, 1, 1, 0]
print(sortcolor(arr))