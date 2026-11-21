class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=0
        rightsum=0
        n=len(nums)
        prefixsum=[0]*n
        currentsum=0
        for i in range(n):
            currentsum+=nums[i]
            prefixsum[i]=currentsum
        for i in range(n):
            leftsum=prefixsum[i-1] if i> 0 else 0
            rightsum=prefixsum[n-1]-prefixsum[i]
            if rightsum==leftsum:
                return i
        return -1
arr=[1,7,3,6,5,6]
print(Solution().pivotIndex(arr))