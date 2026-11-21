
def maxSumSubarray(nums,k):
    window_sum=0
    for i in range(k):
        window_sum+=nums[i]
    max_sum=window_sum
    for i in range(k,len(nums)):
        window_sum=window_sum-nums[i-k]+nums[i]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum
nums=[2,1,5,1,3,2]
k=3
print(maxSumSubarray(nums,k))
