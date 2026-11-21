class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        st=set()
        for i in range(len(nums)):
            if i>k: 
                st.remove(nums[i-k-1]) #removing the element which is out of the range of k from the set
            if nums[i]  in st:
                return True
            st.add(nums[i])
        return False
arr=[1,2,3,1]
k=3
print(Solution().containsNearbyDuplicate(arr,k))