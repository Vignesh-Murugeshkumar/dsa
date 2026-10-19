def countzeroandone(arr):
    count_zero = 0
    count_one = 0

    for num in arr:
        if num == 0:
            count_zero += 1
        elif num == 1:
            count_one += 1

    sorted_arr = [0] * count_zero + [1] * count_one
    return sorted_arr
arr = [0, 1, 0, 1, 1, 0, 0, 1]
print(countzeroandone(arr))