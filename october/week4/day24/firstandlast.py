class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_bound(is_first):
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        high = mid - 1  
                    else:
                        low = mid + 1   
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        return [find_bound(True), find_bound(False)]
def count_occurrences(nums, target):
    first_index = Solution().searchRange(nums, target)[0]
    if first_index == -1:
        return 0
    last_index = Solution().searchRange(nums, target)[1]
    return last_index - first_index + 1
arr=[1,1,2,2,2,3,3,4,5,6,7,8,9]
target=2
print(count_occurrences(arr, target))