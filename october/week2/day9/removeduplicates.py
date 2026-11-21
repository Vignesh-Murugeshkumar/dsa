
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return nums[:k]


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(arr))