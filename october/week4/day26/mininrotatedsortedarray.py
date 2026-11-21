class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low,high=0,n-1
        while  low<high:
            mid=low+(high-low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
nums=[3,4,5,1,2]
print(Solution().findMin(nums))