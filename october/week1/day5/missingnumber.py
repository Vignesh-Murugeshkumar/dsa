class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset=set()
        for num in nums:
            hashset.add(num)
        n=len(nums)
        for i in range(n+1):
            if i not in hashset:
                return i
        return 0
arr=[3,0,1]
print(Solution().missingNumber(arr))