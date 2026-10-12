class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total=0
        left=0
        minlength=float('inf')
        for right in range(len(nums)):
            total+=nums[right]
            while(total>=target):
                minlength=min(minlength,right-left+1)
                total-=nums[left]
                left+=1
        return 0 if minlength==float('inf') else minlength

arr=[2,3,1,2,4,3]
target=7    
print(Solution().minSubArrayLen(target,arr))