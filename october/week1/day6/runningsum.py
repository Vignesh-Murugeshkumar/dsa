class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixsum=[0]*len(nums)
        prefixsum[0]=nums[0]
        for i in range(1,len(nums)):
            prefixsum[i]=nums[i]+prefixsum[i-1]
        return prefixsum
arr=[1,2,3,4]
print(Solution().runningSum(arr))