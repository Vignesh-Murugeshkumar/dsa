class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
            else:
                seen.add(nums[i])
        return seen.pop()
arr = [4,1,2,1,2]
print(Solution().singleNumber(arr))