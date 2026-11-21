
def findMaxAverage(nums,k):
    window_sum=0
    for i in range(k):
        window_sum+=nums[i]
    max_sum=window_sum
    for i in range(k,len(nums)):
        window_sum=window_sum-nums[i-k]+nums[i]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum/k
nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))
