def floorCeil(nums, x):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return [x, x]
        elif nums[mid] < x:
            floor = nums[mid]
            low = mid + 1
        else:
            ceil = nums[mid]
            high = mid - 1
    return [floor, ceil]
nums = [1, 2, 4, 6, 8, 10]
x = 5
print(floorCeil(nums, x))