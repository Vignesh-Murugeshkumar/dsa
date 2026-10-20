class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total=0 
        left=0
        minlength=float('inf') #declareing minlenght to infinity to find the minimum length of the subarray
        for right in range(len(nums)):
            total+=nums[right] #adding the current element to the total sum
            while(total>=target): #if total sum is >=target then we check for the minlenght of the array
                minlength=min(minlength,right-left+1)
                total-=nums[left] #subtracting the leftmost element from the total sum
                left+=1 
        return 0 if minlength==float('inf') else minlength

arr=[2,3,1,2,4,3]
target=7    
print(Solution().minSubArrayLen(target,arr))