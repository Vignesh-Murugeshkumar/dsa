
def sortArrayByParity(nums):
    left=0
    right=len(nums)-1
    while left<right:
        while left<right and nums[left]%2== 0:
            left+= 1
        while left<right and nums[right]%2!=0:
            right-=1
        if left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left += 1
            right -= 1
    return nums
arr = [3, 1, 2, 4]
print(sortArrayByParity(arr))