class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        mid=0
        while mid<=high:
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

arr = [2, 0, 2, 1, 1, 0]
solution = Solution()
print(solution.sortColors(arr))