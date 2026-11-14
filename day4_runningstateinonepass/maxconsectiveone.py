class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum=0
        max_sum=0
        for i in range(len(nums)):
            if nums[i]==1:
                currentsum+=1
                max_sum=max(currentsum,max_sum)
            else:
                currentsum=0
        return max_sum
arr=[1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(arr))