class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set=set()
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            else:
                hash_set.add(nums[i])
        return False
arr = [1,2,3,1]
target = 9
print(Solution().containsDuplicate(arr))