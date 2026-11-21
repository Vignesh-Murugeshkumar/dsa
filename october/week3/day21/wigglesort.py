def wigglesort(nums):
    for i in range(len(nums)-1):
        if i%2==0: 
        #if index is even, then the current element should be less than the next element
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
        else:
        #if index is odd, then the current element should be greater than the next element
            if nums[i]<nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums
arr = [3, 5, 2, 1, 6, 4]
print(wigglesort(arr))