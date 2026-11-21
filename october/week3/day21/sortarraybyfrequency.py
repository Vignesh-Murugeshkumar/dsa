class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if (freq[nums[j]] < freq[nums[min_index]] or
                    (freq[nums[j]] == freq[nums[min_index]] and
                     nums[j] > nums[min_index])):
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

arr = [1, 1, 2, 2, 2, 3]
solution = Solution()   
print(solution.frequencySort(arr))