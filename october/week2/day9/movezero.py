
def moveZeroes(nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    while k < len(nums):
        nums[k] = 0
        k += 1

    return nums


arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))