class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start=0
        zc=0
        maxone=0
        for end in range(0,len(nums)):
            if nums[end]==0:
                zc+=1
            while zc>k:
                if nums[start]==0:
                    zc-=1
                start+=1
            maxone=max(maxone,end-start+1)
        return maxone
arr=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(Solution().longestOnes(arr,k))