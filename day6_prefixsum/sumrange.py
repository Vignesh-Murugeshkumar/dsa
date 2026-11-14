class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n=len(nums)
        self.perfixsum=[0]*(n+1)
        currentsum=0
        for i in range(len(nums)):
            currentsum+=nums[i]
            self.perfixsum[i+1]+=currentsum
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.perfixsum[right+1]-self.perfixsum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
arr=[-2,0,3,-5,2,-1]
obj=NumArray(arr)
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))