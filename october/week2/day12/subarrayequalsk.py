class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map={0:1} #declaring a map to store the sum of the subarray and its count
        count=0
        currentsum=0
        for num in nums:
            currentsum+=num
            if currentsum-k in map: #if the current sum diff is in the map then we will increment the count by the value of the map[currentsum-k]
                count+=map[currentsum-k] #incrementing the count by the value of the map[currentsum-k]
            map[currentsum]=map.get(currentsum,0)+1 #incrementing the count of the current sum in the map
        return count 
array=[1,2,3]
k=3
print(Solution().subarraySum(array,k))